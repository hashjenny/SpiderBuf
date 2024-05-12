from DrissionPage import ChromiumPage

import tool


page = ChromiumPage()
page.get("http://www.spiderbuf.cn/h06/")

tool.save_data_by_session(page=page, file="H06.csv")
