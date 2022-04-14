import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('News Vacuum')

# UNCOMMENT FOR USE
# window_width = 600
# window_height = 400

# # get the screen dimension
# screen_width = root.winfo_screenwidth()
# screen_heigh = root.winfo_screenheight()

# # find the coordinate of upper-left corner of window
# center_x = int(screen_width/2 - window_width/2)
# center_y = int(screen_heigh/2 - window_height/2)

# root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


root.geometry('600x400+50+50')
root.resizable(False, False)
root.attributes('-topmost', 1)
# root.iconbitmap('./assets/pythontutorial.ico')

ttk.Label(root, text="News Vacuum").pack()


try:
    import ctypes

    ctypes.windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()