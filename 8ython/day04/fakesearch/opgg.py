import requests
from bs4 import BeautifulSoup

'''
document.querySelector("#GameAverageStatsBox-summary > div.Box > table > tbody > tr:nth-child(1) > td:nth-child(1) > div")
#GameAverageStatsBox-summary > div.Box > table > tbody > tr:nth-child(1) > td:nth-child(1) > div
'''
url = "https://www.op.gg/summoner/userName=cuzz"
res = requests.get(url)
doc = BeautifulSoup(res.text, "html.parser")
aa = doc.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins").text

print(aa[:-1])