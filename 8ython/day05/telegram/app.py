from flask import Flask,render_template,request
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from decouple import config
from random import sample
import os
import sys

app = Flask(__name__)

usrs_id = []
bot_token = config('TELEGRAM_TOKEN')
chat_id = config('CHAT_ID')


@app.route("/")
def home():
    return render_template('home.html')


# @app.route("/telegram")
# def telegram():
#     # 이건 서버가 없을때
#     # base_url = "https://api.telegram.org"
#     # method = "getUpdates"

#     # get_url = f"{base_url}/bot{bot_token}/{method}"
#     # response = requests.get(get_url).json()

#     # chat_id = response["result"][0].get("message").get("from").get("id")
#     # usrs_id.append(chat_id)

#     text = request.args.get("text")

#     base_url = "https://api.telegram.org"
#     sendMessage = 'sendMessage'

#     url = f"{base_url}/bot{bot_token}/{sendMessage}?chat_id={chat_id}&text={text}"

#     requests.get(url)

#     return render_template('telegram.html')

@app.route(f'/{bot_token}',methods = ["POST"])
def webhook():
    #1.메아리 쳇봇
    #(1)webhook으로 telegram으로 보낸 요청안의 메세지를 받음
    #(2)그대로 전송
    res = request.get_json()
    # print(pprint(res))
    
    chat_id = res.get("message").get("from").get("id")
    usrs_id.append(chat_id)
    text = res.get('message').get("text")
    base_url = "https://api.telegram.org"
    sendMessage = 'sendMessage'
    getFile = 'getFile'
    
    if res.get('message').get("photo") is not None:
        photo_id = res.get('message').get("photo")[-1].get('file_id')
        
        file_res = requests.get(f"{base_url}/bot{bot_token}/{getFile}?file_id={photo_id}")
        photo_file_path = file_res.json().get("result").get('file_path')
        file_url = f"{base_url}/file/bot{bot_token}/{photo_file_path}"

        photo_file = requests.get(file_url, stream = True)
        
        client_id = config("NAVER_ID")
        client_secret = config("NAVER_SECRET")
        
        url = "https://openapi.naver.com/v1/vision/celebrity"
        
        files = {'image': photo_file.raw.read()}
        headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
        
        response = requests.post(url,  files=files, headers=headers)

        text = response.json().get('faces')[0].get('celebrity').get('value')
        text += str(100 * float(response.json().get('faces')[0].get('celebrity').get('confidence'))) + "%"
        
        



    else:
            
            
        if text == "lotto":
            lotto_num = str(sorted(sample(range(1,46),6)))
            text = lotto_num
        elif "search : " in text:
            a = text.find("search : ")
            a = a + 9
            search_base = "https://www.google.com/search?q="
            search_url = search_base + text[a:]
            text = search_url
        elif "/검색 " in text:
            a = text.find("/검색 ")
            a = a + 4
            search_base = "https://www.google.com/search?q="
            search_url = search_base + text[a:]
            text = search_url
        elif "/검색" in text:
            a = text.find("/검색")
            a = a + 3
            search_base = "https://www.google.com/search?q="
            search_url = search_base + text[a:]
            text = search_url
        elif "/번역" in text:
            a = text.find("/번역")
            a = a + 3
            papago_url = "https://openapi.naver.com/v1/papago/n2mt"

            headers = {
                "X-Naver-Client-Id" : config("NAVER_ID"),
                "X-Naver-Client-Secret" : config("NAVER_SECRET") 
            }

            data = {
                "source" : "ko",
                "target" : "en",
                "text" : text[a:]
            }
            text = requests.post(papago_url, headers = headers, data = data).json().get('message').get('result').get("translatedText")
        
    url = f"{base_url}/bot{bot_token}/{sendMessage}?chat_id={chat_id}&text={text}"
    requests.get(url)
    return '', 200

if __name__ == "__main__":
    app.run(debug = True)