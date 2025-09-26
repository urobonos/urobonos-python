import pandas as pd
import yfinance as yf
import shutil
import library.langchain_gemini as gemini

pd.set_option('display.max_rows', None)

# 특정 종목의 데이터 다운로드
#data = yf.download("005930.KS", start="2023-01-01", end="2025-09-26")
#print(data)

#테슬라
#ticker_target = "TSLA"

#삼성
#ticker_target = "005930.KS"

ticker_target = "YMAG"

#data = yf.download(ticker_target, period="30d", interval="1h")
data = yf.download(ticker_target, start="2024-09-26", end="2025-09-26")

yf_chart_data = data.to_string()


# 뉴스 데이터 가져오기
ticker = yf.Ticker(ticker_target)
news = ticker.news



split_line = "="
width = shutil.get_terminal_size().columns  # 현재 콘솔 너비
repeat_count = width // len(split_line) + 1       # 텍스트 반복 횟수 계산
split_text = (split_line * repeat_count)[:width]      # 정확히 화면 너비만큼 자르기
print(split_text)

yf_news_data = data.to_string()


for item in news:
    pubDate = item['content']['pubDate']
    title = item['content']['title']
    summary = item['content']['summary']
    #print(f"{pubDate} - {summary}")
    #print(summary)

    #print(item['title'], item['link'])


print(gemini.request(f"""
                     {ticker_target}의 주가흐름과 뉴스임 
                     {yf_chart_data} // + {yf_news_data}
                    그외 동일기간의 {ticker_target}관련 뉴스와 경제전반 뉴스, 통계청 데이터를 종합추가해서
                    변동일별 상승이유/하락이유와 시계열로 이후 30일간 해당 주가흐름을 시계열로 알려줘
                    예측모델은 여러가지를 사용해서 평균적인 값으로 알려줘
"""))
