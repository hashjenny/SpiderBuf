from DataRecorder import Recorder
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('http://www.spiderbuf.cn/s06/')
iframe = page.get_frame('@src=/inner')

recorder = Recorder(f'S06.csv')

# add head
head = iframe.ele('.table').ele('tag:thead')
row_data = []
for head_item in head.eles('tag:th'):
    row_data.append(head_item.text)
recorder.add_data(row_data)

# add data
for row in iframe.ele('.table').ele('tag:tbody').eles('tag:tr'):
    row_data = []
    for item in row.eles('tag:td'):
        row_data.append(item.text)
    recorder.add_data(row_data)

recorder.record()
