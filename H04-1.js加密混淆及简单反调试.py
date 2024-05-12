from DrissionPage import ChromiumPage

import tool

page = ChromiumPage()
page.get("http://www.spiderbuf.cn/h04/")

# 不知为何，获取页面后使用page.ele()获取页面元素卡顿，使用BeautifulSoup传入page.html解析页面
tool.save_data_by_bs4(page.html, "H04.csv")

page.quit()
