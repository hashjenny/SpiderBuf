from DataRecorder import Recorder
from DrissionPage import SessionPage, ChromiumPage
from bs4 import BeautifulSoup


def save_table_data(page: SessionPage | ChromiumPage, file: str):
    recorder = Recorder(file)

    # add head
    head = page.ele(".table").ele("tag:thead")
    row_data = []
    for head_item in head.eles("tag:th"):
        row_data.append(head_item.text)
    recorder.add_data(row_data)

    # add data
    for row in page.ele(".table").ele("tag:tbody").eles("tag:tr"):
        row_data = []
        for item in row.eles("tag:td"):
            row_data.append(item.text)
        recorder.add_data(row_data)

    recorder.record()


def save_table_data2(page: SessionPage | ChromiumPage, file: str):
    recorder = Recorder(file)

    rows = page.ele(".table").eles("tag:tr")
    for row in rows:
        row_data = []
        if row.ele("tag:th"):
            for item in row.eles("tag:th"):
                row_data.append(item.text)
        else:
            for item in row.eles("tag:td"):
                row_data.append(item.text)
        recorder.add_data(row_data)

    recorder.record()


def save_data_by_bs4(html: str, file: str):
    recorder = Recorder(file)

    soup = BeautifulSoup(html, "html.parser")
    rows = soup.find(attrs={"class": "table"}).find_all("tr")
    for row in rows:
        row_data = []
        if row.find("th"):
            for item in row.find_all("th"):
                row_data.append(item.text)
        else:
            for item in row.find_all("td"):
                row_data.append(item.text)
        recorder.add_data(row_data)

    recorder.record()
