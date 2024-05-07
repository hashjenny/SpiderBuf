from DataRecorder import Recorder
from DrissionPage import SessionPage


def save_table_data(page: SessionPage, file: str):
    recorder = Recorder(file)

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
