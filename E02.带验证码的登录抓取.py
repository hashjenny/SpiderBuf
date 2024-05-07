from DrissionPage import SessionPage

import tool

page = SessionPage()
page.set.cookies(
    'admin=6b48b5442951153da86c85f3338842be; __gads=ID=233e3251676f0fdd:T=1715085166:RT=1715087447:S=ALNI_MbV5-7mZQu3iEGdvjHnCpafYcMa7w; __gpi=UID=00000e117c0d686f:T=1715085166:RT=1715087447:S=ALNI_MbGNsnXYUAhUovCkCs9xCIjS1vvQw; __eoi=ID=0461cee4a97206ca:T=1715085166:RT=1715087447:S=AA-AfjbghQ7_HVV5WJbnM6KVoAWC')
page.post('http://www.spiderbuf.cn/e02/list')

tool.save_table_data(page, file='E02.csv')
