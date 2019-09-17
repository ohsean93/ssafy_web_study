import requests
import bs4

url1="https://www.naver.com/"

response = requests.get(url1).text

document = bs4.BeautifulSoup(response, "html.parser")

# 한개 받을떄 (맨앞)
#rank_one = document.select_one("html body div#PM_ID_ct.wrap div.header div.section_navbar div.area_hotkeyword.PM_CL_realtimeKeyword_base div.ah_list.PM_CL_realtimeKeyword_list_base ul.ah_l li.ah_item a.ah_a span.ah_k").text

#list1 = document.select("html body div#PM_ID_ct.wrap div.header div.section_navbar div.area_hotkeyword.PM_CL_realtimeKeyword_base div.ah_list.PM_CL_realtimeKeyword_list_base ul.ah_l li.ah_item a.ah_a span.ah_k")
list1 = document.select(".ah_k")
list2=[]

#print(list1)

for i in range(20):
    list2 += list1[i]

#print(list2)

rank = int(input("실시간 검색어 몇 위까지? : "))

if rank>20 or rank <= 0:
    print ("1~20의 수를 입력하세요!")
else:
    for i in range(rank):
        print("현재 {0}위 검색어는 : {1}".format(i+1, list2[i]))
