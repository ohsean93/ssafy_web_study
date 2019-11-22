import csv
from decouple import config
import requests
from datetime import date, timedelta
from ast import literal_eval
from pprint import pprint
from time import sleep
from random import random
import os
from bs4 import BeautifulSoup
import json
from collections import OrderedDict


num_of_genres = {
    "가족": 1,
    "공포(호러)": 2,
    "드라마": 3,
    "멜로/로맨스": 4,
    "미스터리": 5,
    "사극": 6,
    "스릴러": 7,
    "액션": 8,
    "어드벤처": 9,
    "판타지" : 10,
    "코미디" : 11,
}


def collect_data_one(targetkey, taregetdatakey, conditionkey = None, condition = None, all_list = 1, **targetdic):
    '''
    변수 설명
    targetkey : dict가 원소인 list명 - 이후 이 dict를 하위 dict로 명명
    taregetdatakey : 수집할 하위 dict의 key값
    conditionkey = None : 하위 dict의 조건 key값
    condition = None : 하위 dict의 조건 value값
    **targetdic : list가 들어있는 dict(상위dict)
    '''
    
    targetkey_data = targetdic.get(targetkey)
    list_targetdata = []

    for tareget in targetkey_data:
        if (conditionkey == None):
            list_targetdata.append(tareget.get(taregetdatakey)) 
            break
        else:
            if tareget.get(conditionkey) and tareget.get(conditionkey) == condition:
                
                list_targetdata.append(tareget.get(taregetdatakey)) 
                break
            
    ans = list_targetdata

    if all_list == 0:
        if len(list_targetdata) == 1:
            ans = list_targetdata[0]
        
    return ans



def collect_data(targetkey, taregetdatakey, conditionkey = None, condition = None,**targetdic):
    '''
    object를 python에서 활용하기 위한 함수
    변수 설명
    targetkey : dict가 원소인 list명 - 이후 이 dict를 하위 dict로 명명
    taregetdatakey : 수집할 하위 dict의 key값
    conditionkey = None : 하위 dict의 조건 key값
    condition = None : 하위 dict의 조건 value값
    **targetdic : list가 들어있는 dict(상위dict)
    '''
    
    targetkey_data = targetdic.get(targetkey)
    list_targetdata = []
    

    for tareget in targetkey_data:
        if (conditionkey == None):
            list_targetdata.append(tareget[taregetdatakey]) 
        else:
            if tareget.get(conditionkey) and tareget.get(conditionkey) == condition:
                list_targetdata.append(tareget[taregetdatakey]) 
            
    return list_targetdata


base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?'
key = config('MOVIETOKEN')

start_date = date(2019,11,13)
movie_data_json = []


with open('boxoffice.csv', mode = 'w', encoding='utf8', newline= '') as f:
    fieldnames = ['movieCd','movieNm','audiAcc']

    csv_writer = csv.DictWriter(f,fieldnames=fieldnames)
    csv_writer.writeheader()

    set_movieCd = set()  

    for week in range(50):
        print(week+1)
        targetdate = start_date - timedelta(days = 7*week)
        targetDt = targetdate.strftime('%Y%m%d')
            
        url = f'{base_url}&key={key}&targetDt={targetDt}&weekGb=0'

        boxoff_weekly_data = requests.get(url).json().get('boxOfficeResult').get('weeklyBoxOfficeList')

        for rank in range(10):
            if boxoff_weekly_data[rank].get('movieCd') in set_movieCd:
                continue
            else: 
                movie_data = {
                    'movieCd' : boxoff_weekly_data[rank].get('movieCd'),
                    'movieNm' : boxoff_weekly_data[rank].get('movieNm'),
                    'audiAcc' : boxoff_weekly_data[rank].get('audiAcc')
                }
                csv_writer.writerow(movie_data)
                set_movieCd.add(boxoff_weekly_data[rank].get('movieCd'))


with open('boxoffice.csv', 'r', encoding = 'utf-8') as f:
    csv_reader = csv.DictReader(f)
    list_moviedata = []
    for row in csv_reader:
        list_moviedata.append((dict(row)['movieCd'], dict(row)['audiAcc'], dict(row)['movieNm']))


with open('movie.csv', mode = 'w', encoding='utf8', newline= '') as f:
    fieldnames = ['title', 'audience','genres','poster_url','description',]
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()

    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?'
    key = config('MOVIETOKEN')

    num = 1 

    client_id = config("NAVER_ID")
    client_secret = config("NAVER_SECRET")
    naver_base_url = 'https://openapi.naver.com/v1/search/movie.json?'

    for movieCd, audience, movieNm in list_moviedata:
        print(f'{num}/{len(list_moviedata)}')
        num += 1
        sleep(round(random(),2))

        url = f'{base_url}&key={key}&movieCd={movieCd}'
        query = movieNm

        naver_url = f'{naver_base_url}query={query}'
        headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
        naver_response = requests.get(naver_url, headers=headers)
        search_data = naver_response.json()
        query = query.replace(' ','')

        for i in search_data.get('items'):
            i['title'] = i.get('title').replace('<b>','').replace('</b>','').replace(' ','')
        
        movie_data = requests.get(url).json()        
        movieInfo = movie_data.get('movieInfoResult').get('movieInfo')
        genres = []

        for genre_name in collect_data('genres', 'genreNm', **movieInfo):
            if num_of_genres.get(genre_name):
                genres.append(num_of_genres.get(genre_name))

        if collect_data_one('items', 'link',conditionkey= 'title',condition = query , all_list=0, **search_data):
            detail_response = requests.get(collect_data_one('items', 'link',conditionkey= 'title',condition = query , all_list=0, **search_data))
        html = detail_response.text
        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup.select('p[class=con_tx]'):
            description = tag.text
            break
        
        data_set = {
            'title': movieInfo.get('movieNm'),
            'audience': audience,
            'poster_url': collect_data_one('items', 'image',conditionkey= 'title',condition = query , all_list=0, **search_data),
            'description': description,
            'genres': genres,
        }
        csv_writer.writerow(data_set)
        row_data = {
            'pk': movieCd,
            'model': 'movies.Movie',
            'fields': data_set
        }
        movie_data_json.append(row_data)
        
with open('movie.json', 'w', encoding="utf-8") as make_file:
    json.dump(movie_data_json, make_file, ensure_ascii=False, indent="\t")