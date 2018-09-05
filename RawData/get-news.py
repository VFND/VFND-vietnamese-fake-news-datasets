from newsplease import NewsPlease

fake_news_urls = ['']

real_news_urls = ['https://news.zing.vn/nhan-chung-ke-lai-phut-doi-mat-voi-ten-cuop-ngan-hang-post874648.html',
                 'https://news.zing.vn/hang-chuyen-phat-nhanh-pha-san-khach-tu-sai-gon-ra-ha-noi-doi-tien-post874640.html',
                 'https://news.zing.vn/go-jek-va-grab-gianh-giat-thi-truong-indonesia-ra-sao-post874114.html']

articles = NewsPlease.from_url('https://news.zing.vn/nhan-chung-ke-lai-phut-doi-mat-voi-ten-cuop-ngan-hang-post874648.html')

print(articles.title)