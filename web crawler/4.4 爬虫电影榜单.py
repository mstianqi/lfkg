import random
import re
import time
import requests
import csv
from lxml import html


TMDB_BASE_URL = "https://www.themoviedb.org"
TMDB_TOP_URL_1 = "https://www.themoviedb.org/movie/top-rated"  # 第一页的网页与剩余页不同
TMDB_TOP_URL_2 = "https://www.themoviedb.org/discover/movie/items"

# 将电影时长转换为分钟
def get_movie_cost_time(times):
    cost_time = times[0].strip() if times else ""
    h_res = re.search(r"(\d+)h", cost_time)
    m_res = re.search(r"(\d+)m", cost_time)
    h = int(h_res.group(1)) if h_res else 0
    m = int(m_res.group(1)) if m_res else 0
    return h * 60 + m

# 保存电影数据
def save_all_movies(all_movies):
    with open("resources/all_movies.csv", "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["电影名","上映时间","时长","评分","语言","导演","主演"])
        writer.writeheader()
        writer.writerows(all_movies)

# 获取单部电影详情
def get_movie_info(movie_info_url):
    # 限制获取数据的频率
    time.sleep(random.uniform(1, 3))

    movie_response = requests.get(movie_info_url, timeout=60)
    movie_doc = html.fromstring(movie_response.text)

    names = movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/a/text()')
    dates = movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="release"]/text()')
    times = movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[@class="runtime"]/text()')
    scores = movie_doc.xpath('//*[@id="consensus_pill"]/div/div[1]/div/div/@data-percent')
    languages = movie_doc.xpath('//*[@id="media_v4"]/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()')
    directors = movie_doc.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()')
    actors = movie_doc.xpath('//*[@id="cast_scroller"]/ol/li[position() <= 2]/p[1]/a/text()')  # 只取前两名主演
    main_actors = "、".join(actor.strip() for actor in actors)

    movie_info = {
        "电影名": names[0].strip() if names else "",
        "上映时间": dates[0].strip() if dates else "",
        "时长": get_movie_cost_time(times),
        "评分": scores[0].strip() if scores else "",
        "语言": languages[0].strip() if languages else "",
        "导演": directors[0].strip() if directors else "",
        "主演": main_actors,
    }
    print(movie_info)
    return movie_info


def main():
    all_movies = []
    # 每页有20部电影
    for page in range(1, 3):
        # 抓取第一页
        if page == 1:
            response = requests.get(
                TMDB_TOP_URL_1,
                params={"language": "zh-CN"},
                headers={
                    "User-Agent": "Mozilla/5.0",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Referer": "https://www.themoviedb.org/",
                },
                timeout=60,
            )
        else:
            # 抓取剩余页
            response = requests.post(
                TMDB_TOP_URL_2,
                params={
                    "language": "zh-CN",
                    "page": page,
                    "sort_by": "vote_average.desc",
                    "vote_count.gte": "300",
                    "watch_region": "CN",
                    "release_date.lte": "2027-02-21",
                },
                timeout=60,
            )

        # 检测 HTTP 请求是否成功，失败会抛出异常
        response.raise_for_status()
        # 使用 response.content 交给 lxml，避免 response.text 的编码判断造成中文乱码，但是直接输出，中文是UTF-8 编码的字节
        document = html.fromstring(response.text)

        # 榜单电影卡片位于 media-list 中；卡片本身有 data-object-id，并包含电影标题 h2。
        # 先根据id查找div元素，然后在其中再查找div元素，满足两个条件，有data-object-id属性和h2元素
        movie_list = document.xpath(
            "//div[@id='media-list']//div[@data-object-id and .//h2]"
        )

        for movie in movie_list:
            # 详情链接位于包含电影 h2 的 a 元素上。
            relative_url = movie.xpath(".//h2/ancestor::a[1]/@href")[0]
            movie_info_url = TMDB_BASE_URL + relative_url

            movie_info = get_movie_info(movie_info_url)
            all_movies.append(movie_info)

    save_all_movies(all_movies)

if __name__ == '__main__':
    main()
