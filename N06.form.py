import json
from pydoc import text
from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get("http://www.spiderbuf.cn/n06")


username_ele = page.ele("#username")
password_ele = page.ele("#password")
email_ele = page.ele("#email")
website_ele = page.ele("#website")
date_ele = page.ele("#date")
time_ele = page.ele("#time")
number_ele = page.ele("#number")
slider_ele = page.ele("#range")
color_ele = page.ele("#color")
search_ele = page.ele("#search")
textarea_ele = page.ele("#textarea")

gender_ele = page.eles("@name=gender")
language_ele = page.eles("@name=interest")
select_ele = page.ele("#country")
ul_select_ele = page.ele(".items").eles("tag:a")

username = username_ele.value
password = password_ele.value
email = email_ele.value
website = website_ele.value
date = date_ele.value
time = time_ele.value
number = int(number_ele.value) if number_ele.value else 0
slider = slider_ele.value
color = color_ele.value
search = search_ele.value
textarea = textarea_ele.value
gender = next(
    (item.after("tag:label").text for item in gender_ele if item.states.is_checked),
    None,
)
language = [
    item.after("tag:label").text for item in language_ele if item.states.is_checked
]
select = [
    item.text for item in select_ele.eles("tag:option") if item.states.is_selected
]
ul_select = next(
    (a.text for a in ul_select_ele if "active" in a.attr("class")),
    None,
)

info = {
    "用户名": username,
    "密码": password,
    "邮箱": email,
    "网站": website,
    "生日": date,
    "时间": time,
    "数量": number,
    "滑块": slider,
    "颜色": color,
    "搜索": search,
    "评论": textarea,
    "性别": gender,
    "开发语言": language,
    "人物代表": select,
    "代表人物出处": ul_select,
}
with open("N06.json", "w", encoding="utf-8") as f:
    json.dump(info, f, ensure_ascii=False, indent=4)

username_ele.clear()
# username_ele.input("username_ele")
username_ele.set.value("username")
password_ele.clear()
password_ele.input("password_ele")
email_ele.clear()
email_ele.input("email_ele@126.com")
website_ele.clear()
website_ele.input("https://www.baidu.com")
date_ele.clear()
date_ele.set.value("1991-11-11")
time_ele.clear()
time_ele.set.value("20:20:20")
number_ele.clear()
# number_ele.input(5)
number_ele.set.value(number_ele.attr("min"))
slider_ele.clear()
slider_ele.set.value(number_ele.attr("min"))
color_ele.clear()
color_ele.set.value("#ffaacc")
search_ele.clear()
search_ele.input("hat")
textarea_ele.clear()
textarea_ele.input("ta")

list(filter(lambda item: item.attr("id") == "gender-female", gender_ele))[0].click()

# language_ele[-2].check(uncheck=True)
[
    item.check(uncheck=True)
    for item in filter(lambda item: "o" in item.attr("id"), language_ele)
]

select_ele.select.by_value("Sanji")
# select_ele.select("娜美")

[a.click() for a in ul_select_ele if a.text == "龙珠"]

page.quit()
