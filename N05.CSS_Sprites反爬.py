from DrissionPage import SessionPage

page = SessionPage()
page.get("http://www.spiderbuf.cn/n05/")

class_map = {
    "sprite abcdef": "0",
    "sprite ghijkl": "1",
    "sprite mnopqr": "2",
    "sprite uvwxyz": "3",
    "sprite yzabcd": "4",
    "sprite efghij": "5",
    "sprite klmnop": "6",
    "sprite qrstuv": "7",
    "sprite wxyzab": "8",
    "sprite cdefgh": "9",
}

items = page.eles(".col-xs-6 col-lg-4")
for item in items:
    company = item.ele("tag:h2").text
    value_eles = item.eles("css:p>.sprite")
    value = [class_map[ele.attr("class")] for ele in value_eles]
    value = int("".join(value))
    print(f"{company}: {value}")
