
from DrissionPage import ChromiumPage

import tool

page = ChromiumPage()
page.get('http://www.spiderbuf.cn/h06/')
page.refresh()
page.wait.ele_displayed('.table')

tool.save_table_data2(page, file='H04.csv')
