import json

from DrissionPage import SessionPage

page = SessionPage()
page.set.encoding('utf-8')
page.get('http://www.spiderbuf.cn/iplist')

with open('S07.json', 'w', encoding='utf-8') as f:
    json.dump(page.json, f, ensure_ascii=False, indent=2)
