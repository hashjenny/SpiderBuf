from DrissionPage import SessionPage

import tool

page = SessionPage()

url = 'http://www.spiderbuf.cn/e03/'
page.get(url)
routers = page.ele('.pagination').eles('tag:a')

# router: <a href="./2fe6286a4e5f">1</a>
# src: http://www.spiderbuf.cn/e03/2fe6286a4e5f
for router in routers:
    src = router.attr('href').split('/')[-1]
    page = SessionPage()
    page.get(url + src)
    tool.save_table_data(page, file='E03.csv')
