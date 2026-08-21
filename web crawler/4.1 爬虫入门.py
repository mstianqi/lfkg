import requests
from lxml import html
from lxml.html import tostring

# target_url = "https://www.tiobe.com/tiobe-index/"
# response = requests.get(target_url)
# document = html.fromstring(response.text)
#
# # 解析表头。xpath查询返回的是列表
# th_list = document.xpath("//*[@id='top20']/thead/tr/th/text()")
# print(th_list)
#
# # 解析表格中的数据
# tr_list = document.xpath("//*[@id='top20']/tbody/tr")
# for tr in tr_list:
#     td_list = tr.xpath("./td/text()")
#     print(td_list)

target_url = "https://www.themoviedb.org/movie/980431-avatar-aang-the-last-airbender"
response = requests.get(target_url)
document = html.fromstring(response.text)
print(tostring(document).decode('utf-8'))