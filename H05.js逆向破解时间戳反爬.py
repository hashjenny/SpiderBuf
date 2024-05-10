from DrissionPage import ChromiumPage

import tool

page = ChromiumPage()
# TODO: http://www.spiderbuf.cn/h05/ 数据目前加载不出来，没法做
page.get("http://www.spiderbuf.cn/h05/")
page.wait.ele_displayed('.table')

tool.save_table_data2(page, file="H05.csv")
