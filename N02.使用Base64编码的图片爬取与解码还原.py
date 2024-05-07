import base64

from DrissionPage import SessionPage

page = SessionPage()
page.get('http://www.spiderbuf.cn/n02/')

img = page.ele('@class:img-responsive')
code = img.attr('src').removeprefix('data:image/png;base64,')
code_bytes = code.encode('raw-unicode-escape')
decoded = base64.b64decode(code_bytes)

with open('N02.png', 'wb') as f:
    f.write(decoded)
