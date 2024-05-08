import json

from DrissionPage import SessionPage

page = SessionPage()
page.get('http://www.spiderbuf.cn/static/js/h04/udSL29.js')

js_code = page.html
start = js_code.index('=')
end = js_code.index(';')
js_code = js_code[start+1:end]

data = eval(js_code)
# for item in data:
#     print(item)

with open('H04.json', 'w', encoding='utf') as f:
    json.dump(data, f, ensure_ascii=False)
