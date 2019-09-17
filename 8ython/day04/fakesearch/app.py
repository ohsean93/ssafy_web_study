from flask import Flask, render_template, request
from faker import Faker
from random import uniform, randint
import requests
from bs4 import BeautifulSoup

fake = Faker("ko_KR")
app = Flask(__name__)

log_job = {}
log_like_name = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/pastlife")
def pastlife():
    return render_template("pastlife.html")

@app.route("/result")
def result():
    name = request.args.get("name")

    if name in log_job.keys():    
        job = log_job[name]
    else:
        job = fake.job()
        log_job[name] = job
    
    return render_template("result.html", name = name, job = job)

@app.route("/goonghap")
def goonghap():
    return render_template("goonghap.html")

@app.route("/destiny")
def destiny():
    name1 = request.args.get("babo")
    name2 = request.args.get("you")
    score = randint(51, 100)

    if (name1 in log_like_name.keys()) :
        if(name2 in log_like_name[name1].keys()):
            score = log_like_name[name1][name2]

        else:
            log_like_name[name1][name2] = score
            if (name2 in log_like_name.keys()) :
                log_like_name[name2][name1] = score
            else:
                log_like_name[name2] = {name1 : score}
    else:
        log_like_name[name1] = {name2 : score}
        if (name2 in log_like_name.keys()) :
            log_like_name[name2][name1] = score
        else:
            log_like_name[name2] = {name1 : score}
            
    
    return render_template("destiny.html", name1 = name1, name2 = name2, score = score)

@app.route("/admin")
def admin():
    all_line = ""
    for name1 in log_like_name:
        line1 = name1 + "\t"
        for name2, score in name1.items:
            line1 += (name2 + str(score))
        all_line += line1
    
    return render_template("admin.html", log = all_line)

@app.route("/opgg")
def opgg():
    return render_template("opgg.html")

@app.route("/entirely")
def entirely():
    username = request.args.get("userName")

    url = "https://www.op.gg/summoner/userName="
    res = requests.get(url + username)
    doc = BeautifulSoup(res.text, "html.parser")
    win = doc.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins").text
    lose = doc.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses").text

    return render_template("entirely.html", username = username, win = win[:-1], lose = lose[:-1])



if __name__ == "__main__":
    app.run(debug = True)