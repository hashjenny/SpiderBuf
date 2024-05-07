from DataRecorder import Recorder
from DrissionPage import SessionPage

page = SessionPage()
page.get('http://www.spiderbuf.cn/h01/')

recorder = Recorder('H01.csv')

# @class指提取网页元素中class属性带有col-xs-6的标签，:为模糊匹配
cards = page.eles('@class:col-xs-6')

head_flag = False
for card in cards:
    head = []
    row_data = []
    for child in card.children():
        pair = child.text.split('：')
        # 判断是否是公司名的h2标签
        if len(pair) <= 1:
            head.append('Name')
        else:
            head.append(pair[0])

        # 判断是否含有css偏移的元素
        if child.eles('tag:i'):
            raw = list(pair[-1])
            raw[0], raw[1] = raw[1], raw[0]
            row_data.append(''.join(raw))
        else:
            row_data.append(pair[-1])

    if not head_flag:
        recorder.add_data(head)
        head_flag = True
    recorder.add_data(row_data)

recorder.record()
