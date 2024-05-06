from DataRecorder import Recorder
from DrissionPage import SessionPage

# 本节页面有5个分页
page = SessionPage()
page.get('http://www.spiderbuf.cn/s04/')

recorder = Recorder(f'S04.csv')

# add head
head = page.ele('.table').ele('tag:thead')
row_data = []
for head_item in head.eles('tag:th'):
    row_data.append(head_item.text)
recorder.add_data(row_data)

# add data
for n in range(1, 6):
    page.get(f'http://www.spiderbuf.cn/s04/?pageno={n}')
    for row in page.ele('.table').ele('tag:tbody').eles('tag:tr'):
        row_data = []
        for item in row.eles('tag:td'):
            row_data.append(item.text)
        recorder.add_data(row_data)

recorder.record()
