from DrissionPage import ChromiumPage

import tool

page = ChromiumPage()
page.get("http://www.spiderbuf.cn/h04/")

tool.save_data_by_bs4(page.html, "H04.csv")

page.quit()
