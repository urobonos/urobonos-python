import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    print("페이지 타이틀:", soup.title.text)
    # 예시: 모든 링크 출력
    for link in soup.find_all('a'):
        print(link.get('href'))
else:
    print("페이지를 불러오지 못했습니다.")
