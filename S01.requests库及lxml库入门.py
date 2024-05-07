from DrissionPage import SessionPage

import tool

page = SessionPage()

page.get('http://www.spiderbuf.cn/s01/')

with open('S01.html', 'w', encoding='utf8') as f:
    f.write(page.html)

tool.save_table_data(page, file='S01.csv')
