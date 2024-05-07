from DrissionPage import SessionPage

import tool

# 本节td标签里面含有a标签和font标签
page = SessionPage()
page.get('http://www.spiderbuf.cn/s03/')

tool.save_table_data(page, file='S03.csv')
