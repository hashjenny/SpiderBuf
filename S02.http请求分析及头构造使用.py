from DrissionPage import SessionPage

import tool

# 本节需要使用浏览器user-agent，不然直接用requests请求会返回403，不过DrissionPage直接请求没问题
# print(requests.get('http://www.spiderbuf.cn/s02/').text)

page = SessionPage()

page.get('http://www.spiderbuf.cn/s02/')

with open('S02.html', 'w', encoding='utf8') as f:
    f.write(page.html)

tool.save_table_data(page, file='S02.csv')

