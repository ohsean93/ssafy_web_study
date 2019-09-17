from flask import Flask, render_template
from random import choice, sample
import bs4
import requests
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', username = name)

@app.route("/menu")
def menu():
    manu_list = {
        "20층" : "http://edu.ssafy.com/data/upload_files/namo/images/000004/20190708082304576_18S6XNQP.png" ,
        "김밥" : "http://recipe1.ezmember.co.kr/cache/recipe/2016/06/29/e83ce1d994ff9b5ffcd1981c8971119d1.jpg", 
        "샌드위치" : "http://recipe1.ezmember.co.kr/cache/recipe/2015/05/17/a38d367db0958c6ab7d29c6a9d4ab62a1.jpg"
        }
    ans = choice(list(manu_list.items()))
    
    return render_template('menu.html', menu = ans[0] , picture = ans[1] )

@app.route("/lotto")
def lotto():
    today = datetime.datetime.now()
    stat_day = datetime.datetime(year = 2002, month = 12, day = 7)
    no_num = (today - stat_day).days//7+1
    
    
    url1="https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="
    
    response = requests.get(url1+str(no_num))
    dic1 = response.json()

    winner = []
    for i in range(1,7):
        winner.append(dic1["drwtNo"+str(i)])

    bnusnum = dic1["bnusNo"]

    print(winner)
    print(bnusnum)
    my_num = sorted(sample(range(1,46),6))

    cor = 0
    bnus_cor = 0

    for j in my_num:
        for i in winner:
            if i == j:
                cor += 1
            if bnusnum == j:
                bnus_cor = 1

    if cor == 6:
        rank = 1
    elif cor == 5:
        if bnus_cor == 1:
            rank = 2
        else:
            rank = 3
    elif cor == 4:
        rank = 4
    elif cor == 3:
        rank = 5
    else:
        rank = 6

    if rank == 6:
        ans = "꽝! 다음 기회에!"
    else:
        ans = f"{rank}위 당첨! 축하합니다!"
    
    return render_template('lotto.html', MyNum = my_num , AnsStr = ans)







if __name__ == "__main__":
    app.run(debug = True)

