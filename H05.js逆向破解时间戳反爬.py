from DrissionPage import ChromiumPage

import tool

page = ChromiumPage()
page.get("http://www.spiderbuf.cn/h05/")

rows = page.ele(".table").eles("tag:tr")
for row in rows:
    row_data = []
    if row.ele("tag:th"):
        for item in row.eles("tag:th"):
            row_data.append(item.text)
    else:
        for item in row.eles("tag:td"):
            row_data.append(item.text)
    print(row_data)
