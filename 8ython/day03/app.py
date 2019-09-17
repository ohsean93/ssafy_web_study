from flask import Flask
import random
import requests
import bs4
from datetime import datetime



app = Flask(__name__)


# 주문 받는 방식
@app.route("/")

#무엇을 제공할지
def hello():
    return "Hello World!"




@app.route("/hi")
def hi():
    return "hi"

@app.route("/name")
def print_name():
    return "OH_Jeasuk"
    
@app.route("/hello/<person>")
def hello2(person):
    return f"hello {person}"

@app.route("/cube/<num>")
def cube(num):
    a = int(num)**3
    a = str(a)
    return a

    
@app.route("/lotto")
def lotto():
    num = range(1, 46)
    lotto_num = random.sample(num, 6)

    return str(sorted(lotto_num))

    
@app.route("/manu")
def namu():
    manu_list = ["20층", "김밥", "샌드위치"]
    ans = random.sample(manu_list, 1)
    return str(ans)

@app.route("/kospi")
def kospi():
    url1="https://finance.naver.com/sise/"

    response = requests.get(url1).text
    document = bs4.BeautifulSoup(response, "html.parser")

    kospi = document.select_one("#KOSPI_now").text
    return "현재 코스피 지수는 : " + kospi


@app.route("/rank")
def rank():
    url1="https://www.naver.com/"

    response = requests.get(url1).text
    document = bs4.BeautifulSoup(response, "html.parser")

    list1 = document.select(".ah_k")
    list2=[]

    for i in range(10):
        list2 += list1[i]
    
    return str(list2)

    
@app.route("/isnewyear")
def isnewyear():
    month = datetime.now().month
    day = datetime.now().date
    if month == 1 and day == 1:
        return "네"
    else:
        return "<h1>아니요<h1>"

    
