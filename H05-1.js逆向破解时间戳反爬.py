from DrissionPage import ChromiumPage

import tool

page = ChromiumPage()
page.get("http://www.spiderbuf.cn/h05/")

tool.save_data_by_bs4(page.html, "H05.csv")

page.quit()
