import requests
import bs4

url1="https://finance.naver.com/sise/"

response = requests.get(url1).text

document = bs4.BeautifulSoup(response, "html.parser")

kospi = document.select_one("#KOSPI_now").text

print("현재 코스피 지수는 : " + kospi)

kosdaq = document.select_one("#KOSDAQ_now").text

print("현재 코스닥 지수는 : " + kosdaq)

kospi200 = document.select_one("#KPI200_now").text

print("현재 코스피200 지수는 : " + kospi200)

