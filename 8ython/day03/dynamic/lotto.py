import requests
from random import sample

url1="https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"

response = requests.get(url1)
dic1 = response.json()

winner = []
for i in range(1,7):
    winner.append(dic1["drwtNo"+str(i)])

bnusnum = dic1["bnusNo"]
rank = 0
count = 0
count_win = [0, 0, 0, 0, 0]

while rank != 1:
    count+=1
    my_num = sample(range(1,46),6)

    cor = 0
    bnus_cor = 0

    # for j in my_num:
    #     for i in winner:
    #         if i == j:
    #             cor += 1
    #         if bnusnum == j:
    #             bnus_cor = 1

    cor = len(set(my_num) & set(winner))


    if cor == 6:
        rank = 1
        count_win[0] += 1
    elif cor == 5:

        for j in my_num:
            if bnusnum == j:
                bnus_cor = 1

        if bnus_cor == 1:
            rank = 2
            count_win[1] += 1
        else:
            rank = 3
            count_win[2] += 1

    elif cor == 4:
        rank = 4
        count_win[3] += 1
    elif cor == 3:
        rank = 5
        count_win[4] += 1
    else:
        rank = 6

    # if rank != 6:
    #     print(f"{rank}위 당첨! 축하합니다!")
    #     print(count)

print(count_win)
per_count_win = []
for i in range(5):
    per_count_win.append(count_win[i]*100/count) 
print(per_count_win)
print(count)


