from DataRecorder import Recorder
from DrissionPage import SessionPage

page = SessionPage()
page.get('http://www.spiderbuf.cn/n01/')

file = 'N01.csv'
recorder = Recorder(file)

# 只写page.eles('.col-xs-6')时，cards为空，必须写2个类
cards = page.eles('.col-xs-6 col-lg-4')

head_flag = False
for card in cards:
    head = []
    row_data = []
    for child in card.children():
        pair = child.text.split('：')
        if len(pair) <= 1:
            head.append('Name')
        else:
            head.append(pair[0])
        row_data.append(pair[-1])
    if not head_flag:
        recorder.add_data(head)
        head_flag = True
    recorder.add_data(row_data)

recorder.record()
