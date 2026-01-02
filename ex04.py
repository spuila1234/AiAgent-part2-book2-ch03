import requests
import pandas as pd
from datetime import datetime

url = "https://hn.algolia.com/api/v1/search"
params = {
    "query": "AI",
    "tags": "story"
}

response = requests.get(url, params=params)

"""
print(response.status_code)
print(response.json().keys())
"""

data = response.json()
articles = data["hits"]

"""
for article in articles:
    title = article.get("title")
    created_at = article.get("created_at")
    print(title, created_at)
"""

structured_data = []

for article in articles:
    structured_data.append({
        "title": article.get("title"),
        "author": article.get("author"),
        "date": article.get("created_at"),
        "url": article.get("url")
    })
    
df = pd.DataFrame(structured_data)
df["collected_at"] = datetime.now()
print(df.head())

df.to_csv("news_daily.csv", index=False, encoding="utf-8")
print("데이터 수집 및 저장 완료")

