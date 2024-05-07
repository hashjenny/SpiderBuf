import time

from DrissionPage import SessionPage

import tool

page = SessionPage()
url = 'http://www.spiderbuf.cn/n03/'

for i in range(1, 21):
    page.get(f'{url}{i}')
    tool.save_table_data(page, file='N03.csv')
    time.sleep(2.0)
