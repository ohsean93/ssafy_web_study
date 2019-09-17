오프라인에서 활용 가능한 기능

Flack



## 좀더 복잡한 Task해 보자

### 코스피 지수 확인하기

먼저 우리가 하는 일을 step별로 나누어 보자

1. 네이버에 들어가자
2. 검색
3. 정보 획득 및 복사
4. 저장



## 서비스의 패턴

주문/요청 => 응답

web서비스는 요청은 URL을 통해 요청하고 URL을 통해 응답을 받는다.





### 코드 가져오기(패키지 이용법)

pip이용

`pip list` 를 배쉬에 입력하면 설치된 pip 리스트를 확인 가능하다.

설치는 `pip installs 패키지명`



### requests 패키지

`requests.get(URL)` URL에 접속

반환값에 대해서는

http status code에서 확인

`.text`는 html 문서를 출력



### BeautifulSoup 패키지

```python
import requests
import bs4

url1="https://finance.naver.com/sise/"

response = requests.get(url1).text

document = bs4.BeautifulSoup(response, "html.parser")

kospi = document.select_one("#KOSPI_now").text

print("현재 코스피 지수는 : " + kospi)

```



