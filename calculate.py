# 计算B站分P视频时长

import requests
from datetime import timedelta

bvid = "BV1sHU9BmEne"
start_p = 120
end_p = 136

url = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.bilibili.com/"
}

response = requests.get(url, headers=headers, timeout=15)

print("状态码：", response.status_code)
print("返回内容：", response.text[:200])

try:
    result = response.json()
except ValueError:
    print("接口没有返回 JSON，请检查网络、BV号或是否被限流。")
    raise SystemExit

if result.get("code") != 0:
    print("B站接口错误：", result)
    raise SystemExit

pages = result["data"]["pages"]

total = sum(
    page["duration"]
    for page in pages
    if start_p <= page["page"] <= end_p
)

print(f"从第{start_p}P到第{end_p}P的总时长：{timedelta(seconds=total)}")