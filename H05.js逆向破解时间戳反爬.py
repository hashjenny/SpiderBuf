import json
from DrissionPage import SessionPage

import hashlib
import base64
import time

url = "http://www.spiderbuf.cn/h05/api/"

timestamp = str(int(time.time()))
md5_hash = hashlib.md5()
md5_hash.update(timestamp.encode("utf-8"))
md5 = md5_hash.hexdigest()
s = f'{timestamp},{md5}'
payload = str(base64.b64encode(s.encode("utf-8")), encoding="utf-8")

page = SessionPage()
page.get(f"{url}{payload}")

with open('H05.json', "w", encoding="utf-8") as f:
    json.dump(page.json, f, ensure_ascii=False, indent=4)
