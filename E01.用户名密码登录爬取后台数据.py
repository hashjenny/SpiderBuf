from DrissionPage import SessionPage

import tool

page = SessionPage()
payload = {'username': 'admin', 'password': '123456'}
page.post('http://www.spiderbuf.cn/e01/login', data=payload)

tool.save_table_data(page, file='E01.csv')
