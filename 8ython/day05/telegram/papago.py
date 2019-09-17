import requests
from decouple import config
from pprint import pprint

papago_url = "https://openapi.naver.com/v1/papago/n2mt"

headers = {
    "X-Naver-Client-Id" : config("NAVER_ID"),
    "X-Naver-Client-Secret" : config("NAVER_SECRET") 
}

data = {
    "source" : "ko",
    "target" : "en",
    "text" : "자동차"
}
text = requests.post(papago_url, headers = headers, data = data).json().get('message').get('result').get("translatedText")