import json
import os.path

from DrissionPage import SessionPage


class MovieInfo:
    def __init__(self, t: str):
        self.title = t
        self.score = 0.0
        self.director: str = ''
        self.writer: [str] = None
        self.main_character: str = ''
        self.actors: [str] = None
        self.types: [str] = None
        self.country: [str] = None
        self.lang: [str] = None
        self.public_date: [str] = None,
        self.length: [str] = None
        self.aka: [str] = None
        self.imdb: str = ''
        self.profile: str = ''


page = SessionPage()
# url =
page.get('http://www.spiderbuf.cn/h02/')

elems = page.eles('.col-xs-12 col-lg-12')
movie_items: [list] = []
movie_item = []
for ele in elems:
    movie_item.append(ele)
    if len(movie_item) == 2:
        movie_items.append(movie_item)
        movie_item = []

movies: [MovieInfo] = []
for item in movie_items:
    title: str = item[0].ele('tag:h2').text
    movie = MovieInfo(t=title)
    context = item[0].ele('.col-xs-9 col-lg-9').text.split('\n')
    for paragraph in context:
        if paragraph:
            '''
            豆瓣电影评分: 9.6
            导演: 陈凯歌
            编剧: 芦苇 /芦苇 / 李碧华
            主演: 张国荣 /张国荣 / 张丰毅 / 巩俐 / 葛优 / 英达 / 蒋雯丽 / 吴大维 / 吕齐 / 雷汉 / 尹治 / 马明威 / 费振翔 / 智一桐 / 李春 / 赵海龙 / 李丹 / 童弟 / 沈慧芬 / 黄斐 / 徐杰
            类型: 剧情 /剧情 / 爱情 / 同性
            制片国家/地区: 中国大陆 /中国大陆 / 中国香港
            语言: 汉语普通话
            上映日期: 1993-07-26(中国大陆) /1993-07-26(中国大陆) / 1993-01-01(中国香港)
            片长: 171分钟/171分钟/ 155分钟(美国剧场版)
            又名: 再见，我的妾 /再见，我的妾 / Farewell My Concubine / Adieu Ma Concubine
            IMDb: tt0106332
            '''
            [key, value] = paragraph.split(':', maxsplit=1)
            match key:
                case '豆瓣电影评分':
                    movie.score = float(value)
                case '导演':
                    movie.director = value
                case '编剧':
                    movie.writer = [x.strip() for x in value.split('/')]
                case '主演':
                    names = value.split('/')
                    movie.main_character = names[0]
                    movie.actors = [x.strip() for x in names[1:]]
                case '类型':
                    movie.types = [x.strip() for x in value.split('/')]
                case '制片国家/地区':
                    movie.country = [x.strip() for x in value.split('/')]
                case '语言':
                    movie.lang = [x.strip() for x in value.split('/')]
                case '上映日期':
                    movie.public_date = [x.strip() for x in value.split('/')]
                    # for public_date in lst:
                    #     region = re.findall(r"\((.*?)\)", public_date)[0]
                    #     source_date = public_date.split('(')[0]
                    #     dt = datetime.datetime.strptime(source_date, "%Y-%m-%d")
                case '片长':
                    movie.length = [x.strip() for x in value.split('/')]
                case '又名':
                    movie.aka = [x.strip() for x in value.split('/')]
                case 'IMDb':
                    movie.imdb = value
                case _:
                    raise Exception('other info')
    profile = item[1].text.removeprefix('简介：')
    movie.profile = profile

    img = item[0].ele('tag:img').attr('src')
    filename = '_'.join(title.split())
    if not os.path.exists(f'./H02/{filename}.jpg'):
        page.download(img, f'./H02/', rename=f'{filename}.jpg')

    movies.append(movie)

movie_dicts = [vars(x) for x in movies]

with open('./H02.json', 'w', encoding='utf-8') as fp:
    json.dump(movie_dicts, fp, ensure_ascii=False)
