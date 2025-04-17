import requests
import csv
from datetime import datetime

url = "https://newsapi.org/v2/top-headlines"
params = {
    "country": "us",
    "category": "technology",
    "apiKey": "6d61b944ed6045dc8802d7c113f70e21"}

r = requests.get(url, params=params)

if r.status_code != 200:
    print("website is down")

else:
    data = r.json()

    with open("news.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Description", "Link", "Content", "Time"])
        print(data)
        for article in data['articles']:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            title = article['title']
            desc = article['description']
            link = article['url']
            content = article['content']

            writer.writerow([title, desc, link, content, time])
