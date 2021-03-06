# django

2005년07월 탄생

이후

2008 v1.0

2017 v2.0

읽는 방식이 매우 많지만 이 문서에서는 장고로 통일한다.



## 장고의 특징

장고 개발자들이 뽑는 장고의 특징은 다음과 같다.

Versatile - 다용도의

Secure - 안전한

Scalable - 확장성 있는

Complete - 완결성 있는

Maintainable - 쉬운 유지보수

Portable -  포터블한



## 장고의 성격

### 프레임 워크의 두 가지 분류

Opinionated - 독선적인 : 프레임 워크의 규칙을 많이 만들어 사용 자유롭지는 않지만 배우기는 쉽다.

Unopinionated - 관용적 : 프레임 워크의 규칙이 거의 없음 자유로우나 배우기 힘들다.

장고는 '다소 독선적'이다.



## 웹 서비스의 기본

웹 서비스의 기본은 (사실 모든 서비스는) '요청' 후 '받음'으로 구분이 된다.

이떄 웹에서는 요청을 주고 받을 때 사용하는 형식은 url이다. 즉 하나의 요청은 하나의 응답으로 처리된다.



이런 서비스를 바닥부터 구현이 가능하지만, 대체로 규격이 잡힌 프레임 워크를 많이 사용한다.



### 프레임 워크의 구분

하나의 url 패턴은 하나의 함수로서 작용되는데

경량형 프레임 워크는 이런 패턴들을 하나하나 정의를 해서 사용을 한다. 이런 방식은 프레임 워크의 로직이 간단하고, 기능이 많지 않은 가벼운 서비스에 어울린다.(그래서 경량형 프레임워크라고 한다.) 파이썬으로 가능한 경량형 프레임 워크는 플라스크가 있다.

하지만 서비스가 많아지면 이를 유사한 기능 또는 분류끼리 묶는 작업을 하면 관리상, 그리고 개발상의 이점이 생긴다. 그래서 유사한 패턴을 묶는 프레임 워크, 풀 스택 프레임 워크를 사용하게 된다. 파이썬의 풀 스텍 프레임 워크 중 가장 유명한 것이 바로 장고이다.



## MVC / MTV

일반적인 프레임 워크에서는 MVC가 표준으로 쓰이지만 장고는 이를 재해석한 MTV를 사용한다.

Model - 데이터를 관리

Template - 사용자가 보는 화면

View - 중간 관리자



## 장고 명령어

`django-admin  startproject [프로젝트 명]` : 프로벡트 실행

`python manage.py runserver` : 서버 실행

`python manage.py startapp [app명]` : app을 만든다. 기본적으로 1개 이상의 app이 필요하다.

`python manage.py shell` : DB모드로 전환

`python manage.py makemigrations` : DB의 청사진을 그리는 명령어로 models.py의 변경이 있으면 작동한다.

`python manage.py migrate` : DB의 청사진을 적용하는 명령어



## 장고의 (관례적인)구조

PROJECT(대문자)

프로젝트에 관련된 모든 것을 집어 넣는 root폴더

- project(소문자)

  프로젝트 관리 파일의 모임

  - `setting.py`

    - 이 프로젝트에 쓰이는 세팅을 저장한 파일

    - app을 추가도 관리한다.

  - `urls.py`

    일명 문지기 이것을 이용해 요청해 오는 url 을 분류한다.

  - `wsgi.py`

- manage.py :  주 실행 파일

- media : 사진이나 동영상등 유저가 올린 데이터 중 텍스트 형식이 아니라 DB에 들어가기 어려운 파일들의 모음

- app 1 게시판

  기능별 묶인 파일들

  - migrations

  - templates

    사용자에게 보여줄 각종 html 파일들이 들어있는 폴더

    - app 1
      - `XXX.html`

  - `admin.py`

  - `apps.py`

  - `models.py`

    데이터를 저장하는 파일

  - `tests.py`

  - `urls.py`

  - `views.py`

    중간관리자 요청을 처리

- app 2 회원관리

- app 3 영화평점





### 기본적인 django app의 실행 구조

|               기본적인 django app의 실행 구조                |
| :----------------------------------------------------------: |
|                       uesr의 요청(url)                       |
| `urls.py`에서 이를 검토 유효하면 이를 해당하는 app에 `veiws.py`로 전송 |
| `veiws.py`에서는 이를 처리하여 데이터를 해당 template로 전송 |
|      template의 해당 html은 이를 처리하여 사용자에 전송      |



**이 순으로 페이지를 구성한다.**



### 간단한 기능의 페이지를 만들어 보자!

**이 기능은 python 3.7이상을 기준으로 작성되어있다.**

먼저 django 프로젝트를 생성

```bash
mkdir FIRST_APP
cd FIRST_APP
django-admin startproject first_app .
```

이어서 app을 추가하고 서버를 돌려보자

```bash
python manage.py startapp pages
python manage.py runserver
```

서버를 돌리고 확인해야 할 곳은 바로 http://localhost:8000이다.

잘 돌아가면  일단 `ctrl+c`로 종료한뒤 코드를 열어 코드를 수정하자.



제일 먼저 수정할 곳은 `setting.py` 이다. 파일 내에 다음과 같은 리스트가 선언되어있다.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

...

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

이 부분은 이 프로젝트가 실행되는 app들의 리스트이다.



놀랍게도 app을 추가한다고 이 부분이 바뀌지는 않는다.

즉 지금의 상태는 app이 생성되었으나 그 기능을 연결하지는 않은 상태인 것이다!



고로 수동으로 추가하자!



또한 templates의 호환성 문제로 인해 다음과 같이 TEMPLATES에 경로를 추가해 준다.

```python
INSTALLED_APPS = [
    'pages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

...

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR , 'first_app', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

관례상 추가엡은 맨 앞에 넣는다. **쉼표주의** ***진짜 주의*** (지금까지 리스트에 값을 넣었을 때 ','를 안 넣었기 떄문에 은근 많이 빼먹는다.) 이 작업은 햇갈리니까 app을 만들면 바로 바로 해주자(혹 미 구현 기능이면 주석으로 빼자)



그 다음은  `urls.py`를 수정해야 한다.

```python
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
]
```

이쯤해서 다시 처리 구조를 보자



|               기본적인 django app의 실행 구조                |
| :----------------------------------------------------------: |
|                       uesr의 요청(url)                       |
| `urls.py`에서 이를 검토 유효하면 이를 해당하는 app에 `veiws.py`로 전송 |
| `veiws.py`에서는 이를 처리하여 데이터를 해당 template로 전송 |
|      template의 해당 html은 이를 처리하여 사용자에 전송      |



사실 여기서 ' `urls.py`에서 이를 검토 유효하면 이를 해당하는 app에 `veiws.py`로 전송'을 조금 수정해야 한다.

python에서는 외부 파일에 데이터를 넘겨서 코드를 실행하기 위해서는 함수를 호출하여 데이터를 넘겨 주어야 한다. 즉 하위 폴더 [app의 이름]에 있는 파이썬 파일 views.py를 불러와야 한다.

이때 사용되는 로직은  ' `urls.py`에서 이를 검토하여, 유효하면 이를 해당하는 app에 `veiws.py`의 함수를 호출'이라고 보아야 한다. 그럼 이 `urls.py`에서는 path 함수를 통해 유효성 검사가 먼저 시행되고, 이후 함수의 호출이 이루어 진다.

호출되는 함수의 위치는 `/[app명]/view.py`에 있고, 이 함수를 호출하기 위해서는 python 페키지 선언법에 따라 파일의 위치를 선언해야 한다.(혹 함수까지 호출하지 않는 것을 물어보시면, 이는 직관성을 살리기 위해서라고 할 수 있다.(from [app명] import views)

우리는 `/pages/view.py`를 사용할 것이므로 이를

```python
from django.contrib import admin
from django.urls import path
from pages import views
```

와 같이 선언해 주자



그 다음은 'url을 검토하고' 이를 '해당하는 함수로 보내주는' path 함수이다.

이를 각각 인자로 받아 path('[허용 url]/',views.[호출 함수명]) 형식으로 넣어준다.

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('cube/<int:num>/', views.cube),
]
```

눈치가 빠르신 분들은 조금 불편한게 있을 것이다. 그건 일반적인 리스트 선언과 달리 각 element 뒤에 ','가 붙어 있다는 점이다. 이는 python에서 허용하는 부분이고 이를 [    ]라고 한다.

get으로 받을 때를 위해서 <>로 추가 데이터를 받을 수 있다.(하지만 보안상 문제로 안하는게 좋다.)



그럼 이제 `views.py`에 가서 함수를 정의하자

```python
from django.shortcuts import render

# Create your views here.
```

여기에 하나씩 넣자



```python
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def cube(request, num):
    context = {
        'result': num**3,
    }
    return render(request, 'cube.html', context)
```



여기서 잠깐!

render의 역활은 무엇일까?

이를 프린트 하면 `HttpResponse`클레스로 나온다.



이는 `from django.http import HttpResponse`로 `HttpResponse`함수를 이용해 직접 생성할수있다.(하지않는다)

------

# 장고로 계시판을 만들기

1. Models

2. Workflow
   - urls
   - views
   - templates



python Pillow



view는 흘러가는 곳! 따라서 model에서 처리하는 model fat 하게 짜자!



meta : 상위개념의 것

사진에 대한 데이터(위치 시간 크기 확장자 등등) => meta에 저장

model도 meta클레스 정의가 가능하다.

```python
	class Meta:
        ordering = ['-pk',]
```



`ImageField`

`blank=True`옵션 필수

form에 `multipart/form-data` 추가

저장위치 넣기

위치를 db에 넣기

파비콘(favicon-generator)

{% load static %}