import pandas as pd
import yfinance as yf
import shutil


pd.set_option('display.max_rows', None)

# 특정 종목의 데이터 다운로드
#data = yf.download("005930.KS", start="2023-01-01", end="2025-09-26")
#print(data)

#테슬라
#ticker_target = "TSLA"

#삼성
ticker_target = "005930.KS"

# 애플 주식, 최근 5일, 1분 단위
#data = yf.download(ticker_target, period="3d", interval="1h")
data = yf.download(ticker_target, start="2000-01-01", end="2025-09-26")
print(data)

#quit()

# 뉴스 데이터 가져오기
ticker = yf.Ticker(ticker_target)
news = ticker.news

split_line = "="
width = shutil.get_terminal_size().columns  # 현재 콘솔 너비
repeat_count = width // len(split_line) + 1       # 텍스트 반복 횟수 계산
split_text = (split_line * repeat_count)[:width]      # 정확히 화면 너비만큼 자르기
print(split_text)

for item in news:
    pubDate = item['content']['pubDate']
    title = item['content']['title']
    summary = item['content']['summary']
    print(f"{pubDate} - {summary}")
    #print(summary)

    #print(item['title'], item['link'])
