from cmath import exp
from fileinput import filename
import os, json
from newsplease import NewsPlease
import PySimpleGUI as sg

# Version 0.1: News Vacuum MVP

class NewsData():
    def __init__(self):
        self.log = ""
        self.readme = ""
        pass

    def set_url_list(self, url_list):
        self.url_list = url_list

    def set_file_path(self, file_path):
        self.file_path = file_path

    def set_json_prefix(self, json_prefix):
        self.json_prefix = json_prefix
    
    def set_json_start_no(self, json_start_no):
        self.json_start_no = json_start_no

    def update_log(self, message):
        self.log = self.log + message
    
    def update_README(self, readme_text):
        self.readme = self.readme + readme_text

    # Technical Debt: Need checking and exception
    def processing(self):
        self.news_list = self.get_news_to_list()
        self.dump_news_to_json()
        

    def get_news_to_list(self):
        news_list = []
        for url in self.url_list:
            try:
                news_list.append(NewsPlease.from_url(url))
                self.update_log('Done [news] => [list]: ' + url + '...\n--------------\n')
            except Exception as e: 
                self.update_log(str(e) + ': ' + url  + '\n--------------\n')
                continue
        return news_list

    def dump_news_to_json(self):
        file_no = int(self.json_start_no)

        readme_text = ""

        for news in self.news_list:
            try:
                file_name = self.json_prefix + str(file_no) + '.json' 
                
                with open(os.path.join(self.file_path, file_name), 'w', encoding='utf-8') as outfile:
                    json.dump(news.__dict__, outfile, indent=4, sort_keys=True, default=str, ensure_ascii=False)

                self.update_log('News -> JSON: ' + str(file_name) + '\n--------------\n')
                
                news_dict = news.__dict__
                readme_text = readme_text + self.json_prefix + str(file_no) + ": [" + news_dict['title'] + "](" + news_dict['url'] + ")\n\n"
                
                file_no += 1

            except Exception as e:
                news_url = news.get_dict()['url']
                self.update_log(str(e) + ": " + news_url + '\n--------------\n')
                continue

        self.update_README(readme_text)

def main():
    sg.theme('DarkBlue2')

    upper_row = [
        [sg.Text('Save Folder: ', s=20), sg.In(size=(50,2), enable_events=True ,key='-FOLDER-'), sg.FolderBrowse(size=(10,1))],
        [sg.Text('JSON Prefix: ', s=20), sg.In(size=(50,2), enable_events=True, key='-PREFIX INP-')],
        [sg.Text('JSON Start No.: ', s=20), sg.In(size=(50,2), enable_events=True, key='-START INP-')],
        # [sg.Button('Save Profile'), sg.Button('LoadProfile')]
    ]

    left_col = [[sg.Text('News URL List (1 URL/line): ')],
                [sg.Multiline(enable_events=True, size=(40,20), key='-URLLIST INP-')]]

    right_col = [[sg.Text('Result:')],
                [sg.Multiline(font='Courier 10', key='-OUTPUT-', size=(40,20), expand_x=True, expand_y=True, reroute_cprint=True, write_only=True, autoscroll=True)]
                ]

    below_row = [
        [sg.Button('START VACUUM PROCESS', expand_x=True, key='-START PROCESS-')]
    ]

    # ----- Full layout -----
    layout = [
        [sg.Column(upper_row)],
        [sg.Column(left_col), sg.VSeperator(), sg.Column(right_col)],
        [below_row]
    ]

    # --------------------------------- Create Window ---------------------------------
    window = sg.Window('VFND NEWS VACUUM', layout)
    controler = NewsData()

    # ----- Run the Event Loop -----
    # --------------------------------- Event Loop ---------------------------------
    while True:
        event, values = window.read()
        
        if event in (None, 'Exit'):
            break
        if event == '-FOLDER-':
            folder = values['-FOLDER-']            
            controler.set_file_path(folder)
            
        elif event == '-PREFIX INP-':
            json_prefix = values['-PREFIX INP-']
            controler.set_json_prefix(json_prefix)

        elif event == '-START INP-':
            # Technical Debt: Need to check type of input
            json_start = values['-START INP-']
            controler.set_json_start_no(json_start)            

        elif event == '-START PROCESS-':
            # Technical Debt: No checking at the moment
            url_list_str = values['-URLLIST INP-']
            url_list = url_list_str.split('\n')
            
            controler.set_url_list(url_list)
            window['-OUTPUT-'].update(controler.log)

            controler.processing()
            window['-OUTPUT-'].update(controler.log)

            readme_log = controler.log + "\nUPDATE README.md------------------- \n" + controler.readme
            window['-OUTPUT-'].update(readme_log)

    window.close()
    # --------------------------------- Close & Exit ---------------------------------

if __name__ == '__main__':
    main()