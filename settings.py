from DrissionPage import ChromiumOptions, ChromiumPage


co = ChromiumOptions()

# 阻止“自动保存密码”的提示气泡
co.set_pref("credentials_enable_service", False)

# 阻止“要恢复页面吗？Chrome未正确关闭”的提示气泡
co.set_argument("--hide-crash-restore-bubble")

page = ChromiumPage(co)
