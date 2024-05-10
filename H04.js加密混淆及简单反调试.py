import json

from DrissionPage import SessionPage

page = SessionPage()
page.get('http://www.spiderbuf.cn/static/js/h04/udSL29.js')

'''
var data = [{
    "\u0069\u0064": 0x1,
    "\u0072\u0061\u006e\u006b\u0069\u006e\u0067": 0x1,
    "\u0070\u0061\u0073\u0073\u0077\u0064": "\u0070\u0061\u0073\u0073\u0077\u006f\u0072\u0064",
    "\u0074\u0069\u006d\u0065\u005f\u0074\u006f\u005f\u0063\u0072\u0061\u0063\u006b\u005f\u0069\u0074": '<\x201\x20Second',
    "\u0075\u0073\u0065\u0064\u005f\u0063\u006f\u0075\u006e\u0074": 0x4b3659,
    "\u0079\u0065\u0061\u0072": 0x7e6
}, ...{...}];
'''
js_code = page.html
start = js_code.index('=')
end = js_code.index(';')
js_code = js_code[start+1:end]

data = eval(js_code)
# for item in data:
#     print(item)

with open('H04.json', 'w', encoding='utf') as f:
    json.dump(data, f, ensure_ascii=False)
