from DrissionPage import SessionPage

page = SessionPage()
page.get('http://www.spiderbuf.cn/s05/')
img_lst = page.ele('.table-responsive').eles('tag:img')

for img in img_lst:
    url = img.attr('src')
    page.download(url, r'.\S05imgs')
