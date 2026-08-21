import requests
import csv
from lxml import html


TMDB_BASE_URL = "https://www.themoviedb.org"
TMDB_TOP_URL = "https://www.themoviedb.org/movie/top-rated"

# 保存电影数据
def save_all_movies(all_movies):
    pass

# 获取电影详情
def get_movie_info(movie_info_url):
    pass

def main():
    # 访问 TMDB 的“高分电影”榜单第一页。
    response = requests.get(
        TMDB_TOP_URL,
        params={"language": "zh-CN", "page": 1},
        headers={
            "User-Agent": "Mozilla/5.0",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Referer": "https://www.themoviedb.org/",
        },
        timeout=60,
    )
    # 检测 HTTP 请求是否成功，失败会抛出异常
    response.raise_for_status()
    # 使用 response.content 交给 lxml，避免 response.text 的编码判断造成中文乱码。
    document = html.fromstring(response.content)

    # 榜单电影卡片位于 media-list 中；卡片本身有 data-object-id，并包含电影标题 h2。
    # 先根据id查找div元素，然后在其中再查找div元素，满足两个条件，有data-object-id属性和h2元素
    movie_list = document.xpath(
        "//div[@id='media-list']//div[@data-object-id and .//h2]"
    )

    all_movies = []
    for movie in movie_list:
        # 详情链接位于包含电影 h2 的 a 元素上。
        relative_url = movie.xpath(".//h2/ancestor::a[1]/@href")[0]
        movie_info_url = TMDB_BASE_URL + relative_url
        print(movie_info_url)

        # get_movie_info 当前保持为空；得到详情数据后加入总列表。
        movie_info = get_movie_info(movie_info_url)
        all_movies.append(movie_info)

if __name__ == '__main__':
    main()
