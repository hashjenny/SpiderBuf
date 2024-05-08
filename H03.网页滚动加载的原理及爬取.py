from DrissionPage import SessionPage

page = SessionPage()
url = 'http://www.spiderbuf.cn/h03/'
page.get(url)

movies = [x.text for x in page.eles('tag:h2')]


elem = page.ele('#sLaOuol2SM0iFj4d')
# 防止意外死循环
i = 0
while elem and i < 100:
    page.get(f'{url}{elem.text}')
    movies.extend([x.text for x in page.eles('tag:h2')])
    elem = page.ele('#sLaOuol2SM0iFj4d')
    i += 1

print(len(movies))
print(i)
print(movies)
