# Các file CSV

## 1. Phân loại nhị phân 2 label: Fake & Real

2 label để phân loại là: _Fake_ giá trị 1 và _Real_ giá trị 0. Các file và ý nghĩa tên của chúng:

1._[vn_news_226_tlfr.csv]()_: Chứa 226 record dữ liệu bao gồm 2 trường Text và Label. Text tổng hợp từ các tin tức giả và thật từ Facebook và Báo chí, tin tức báo chí sẽ bao gồm phần tiêu đề và nội dung. ```tlfr``` là ```[text, label, fake, real]```
2._[vn_news_223_tdlfr.csv]()_: Chứa 223 record dữ liệu các bài báo và domain name của các trang đã đăng các bài báo đó. ```tdlfr``` là ```[text, domain, label, fake, real]```