import json
from DrissionPage import ChromiumPage, SessionPage, ChromiumOptions

co = ChromiumOptions()
co = co.set_argument("--no-sandbox")  # 关闭沙箱模式, 解决`$DISPLAY`报错
co = co.set_headless(True)  # 开启无头模式, 解决`浏览器无法连接`报错
page = ChromiumPage(co)
page.get("http://www.spiderbuf.cn/n04/")

movies = []
boxes = page.eles(".col-xs-12 col-lg-12")
for box in boxes:
    if box.ele("tag:h2"):
        title = box.ele("tag:h2").text
        score_ele = box.ele(".col-xs-9 col-lg-9").eles("tag:span")[1]
        # score_ele.pseudo.before -> '"9"'
        prefix = score_ele.pseudo.before.replace('"', "")
        subfix = score_ele.pseudo.after.replace('"', "")
        score = float(f"{prefix}.{subfix}")
        movies.append({"title": title, "score": score})
    else:
        continue

with open("N04.json", "w", encoding="utf-8") as f:
    json.dump(movies, f, ensure_ascii=False, indent=4)

page.quit()
