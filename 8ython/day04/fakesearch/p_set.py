'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}


# 아래에 코드를 작성해 주세요.

sum_score = 0
for i in score.values():
    sum_score += i
mean = sum_score/3

print(f'==== Q1 ====\n{mean}')
print(sum(score.values())/len(score.keys()))


# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.

sum_score = 0
for class_name in scores.keys():
    sum_score += sum(scores[class_name].values())
mean2 = sum_score/(len(scores.keys())*len(scores['a'].keys()))

print(f'==== Q2 ====\n{mean2}')


# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.

print('==== Q3-1 ====')

for city_name in city.keys():
    mean3 = sum(city[city_name])/len(city[city_name])
    print(f"{city_name} 의 평균 기온은 : {mean3:.02F}")

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

min = 0
max = 0
for city_name in city.keys():
    if min(city[city_name]) < min:
        min_city = city_name
    if max(city[city_name]) < max:
        max_city = city_name

# 플랫슨 중복 리스트를 간단히 itertools
print (f'가장 취웠던 곳 : {min_city}\n가장 더웠던 곳 : {max_city}')
# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?


# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
check = 1
for i in city["서울"]:
    if i == 2:
        print("네")
        check = 0
        break
if check == 1:
    print("아니요")
