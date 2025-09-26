import requests
from bs4 import BeautifulSoup
from library.db_utils import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

query = "SELECT id, target_url FROM crawling_target"
cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    id, target_url = row
    print(f"ID: {id}, TARGET_URL: {target_url}")
    # 여기서 원하는 추가 작업 수행
    response = requests.get(target_url)
    print(response)


exit



if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    print("페이지 타이틀:", soup.title.text)
    for link in soup.find_all('a'):
        href = link.get('href')
        print(href)
        if href:
            cursor.execute("INSERT IGNORE INTO crawled_links (url) VALUES (%s)", (href,))
    conn.commit()
    print("DB 저장 완료!")
else:
    print("페이지를 불러오지 못했습니다.")

cursor.close()
conn.close()
