import requests
from DataRecorder import Recorder
from DrissionPage import SessionPage

# 本节需要使用浏览器user-agent，不然直接用requests请求会返回403，不过DrissionPage直接请求没问题
# print(requests.get('http://www.spiderbuf.cn/s02/').text)

page = SessionPage()

page.get('http://www.spiderbuf.cn/s02/')

with open('S02.html', 'w', encoding='utf8') as f:
    f.write(page.html)

recorder = Recorder(f'S02.csv')

# add head
head = page.ele('.table').ele('tag:thead')
row_data = []
for head_item in head.eles('tag:th'):
    row_data.append(head_item.text)
recorder.add_data(row_data)

# add data
for row in page.ele('.table').ele('tag:tbody').eles('tag:tr'):
    row_data = []
    for item in row.eles('tag:td'):
        row_data.append(item.text)
    recorder.add_data(row_data)

recorder.record()

