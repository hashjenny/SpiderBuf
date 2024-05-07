from DrissionPage import SessionPage

import tool

page = SessionPage()
payload = {'level': 8}
page.post('http://www.spiderbuf.cn/s08/', data=payload)

tool.save_table_data(page, file='S08.csv')
