import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

def fetch_google_scholar_results(start):
    base_url = "https://scholar.google.com/scholar"
    query_params = {
        "q": "PulseGAN",
        "hl": "en",
        "as_sdt": "0,5",
        "start": start
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    results = []  # 用于存储结果的列表

    response = requests.get(base_url, params=query_params, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        divs = soup.find_all("div", class_="gs_r gs_or gs_scl")

        for div in divs:
            result = {}
            h3 = div.find("h3")
            if h3:
                a = h3.find("a")
                if a:
                    title = a.get_text()
                    result["Title"] = title

            gs_a = div.find("div", class_="gs_a")
            if gs_a:
                authors = gs_a.get_text()
                result["Authors"] = authors

            results.append(result)  # 将当前结果添加到列表中
    else:
        print("Error", response.status_code)
    return results  # 返回结果列表


# 存储所有页面的结果
all_results = []
for i in range(0, 110, 10):  # 50 表示要爬取的页面数，每次增加 10 个搜索结果
    results = fetch_google_scholar_results(i)
    all_results.extend(results)
    time.sleep(10)  # 为了避免频繁请求，加入了延时
    print("已经爬取了 {} 个结果".format(len(all_results)))

df = pd.DataFrame(all_results)



# 使用正则表达式提取日期及日期之后的内容，并保存为新的列
date_publisher_pattern = r'(\d{4})(.*)'  # 添加捕获组，括号内是日期和日期之后的内容
extracted = df['Authors'].str.extract(date_publisher_pattern)

# 将提取的结果分配到新的列中
df['Date'] = extracted[0]  # 日期列
df['Publisher'] = extracted[1].str.strip()  # 去除日期之后内容的首尾空格并保存为出版商列

# 删除 Authors 列中的日期和出版商
df['Authors'] = df['Authors'].str.replace(date_publisher_pattern, '', regex=True).str.strip()

# 将 DataFrame 写入 Excel 文件
df.to_excel("google_scholar_results_with_date_publisher.xlsx", index=False)

# # 输出所有结果
# for result in all_results:
#     print(result)