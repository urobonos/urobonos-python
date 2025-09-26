import requests
from bs4 import BeautifulSoup
from library.db_utils import get_db_connection


url = "https://www.naver.com"
response = requests.get(url)

conn = get_db_connection()
cursor = conn.cursor()

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    print("페이지 타이틀:", soup.title.text)
    for link in soup.find_all('a'):
        href = link.get('href')
        print(href)
        if href:
            cursor.execute("INSERT INTO crawled_links (url) VALUES (%s)", (href,))
    conn.commit()
    print("DB 저장 완료!")
else:
    print("페이지를 불러오지 못했습니다.")

cursor.close()
conn.close()
