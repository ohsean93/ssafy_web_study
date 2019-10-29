관계형 데이터 베이스

model

class meta

get_absolute_url

reverse('url', kwargs={'pramiter':data})



shell_plus => setting에 django_extensions 추가







ORM

block

url

bootstrap4

|연산자=> 시간 포멧팅

for

csrf_token





SQL언어를 사용

버클리 데이터 베이스 cs186

디비를 만드는 수업

-----

체계화된 데이터의 모임

파일로 사용해되 되지만 이를 데이터 베이스를 사용하면 좋다.

스키마 : 칼럼의 형식을 정의(제약조건)



----

SQL은 관계형 db의 자료 검색과 관리 데이터베이스 스키마의 생성과 수정, 데이터베이스 객체 접근 조정 관리를 위해 고안

DDL : 데이터를 정의하기 위한 언어

DML : 데이터 저장 수정 삭제 조회를 위한 언어

DCL : 사용자 권한 제어



프로그램 시스템 명령어는 '.'으로 실행(예를들면 exit)

.databases

.tables

SELECT * FROM posts_post;





```sqlite

```

form => model form

auth + m:n + validation         |=> Deploy  +  javascript

cbv



USE_I18N => 국제화

USE_L10N => 지역화



mtv순으로 프로젝트



tdd => 테케를 이용해 



레스트풀 => url패턴 만드는 것과 유사

 https://meetup.toast.com/posts/92 

drf 장고 레스트 프레임워크





embed()함수는 실행 중 이 함수를 만나면 잠시 멈추고 ipython의 shell을 실행





----

10/21 수업



회원가입/로그인(Authentication)

권한관리(Authorization)

Auth모듈이라고 함



http의 단점

stateless(상태를 저장하지 않음)

따라서 상태 저장이 필요함

쿠키와 세션(캐쉬)





유저의 로그인 시도시

서버에서는 과자 부스러기를 유저에게 넘긴다.

이게 취약해서

임시적인 저장된 IP MAC에 쿠키를 취합해 알려줌

=> session

장고의 auth 모듈



User

Abstract Base User => 이걸 기반으로 바꿀수 있다.

Abstract User

user => 아이디(username기반)



UserCreationForm => user CRUD

AuthenticationForm => session CRUD

---

middleware: 핵심기능을 중간에서 중계해주는 소프트웨어



session에 저장된 것

_auth_user_id : 유저아이디



registory

redis 

static/midia파일, css jscode 



----

ORM에서 WHERE은

get(조건값) => WHERE 조건값 LIMIT 1

filter(조건값) => WHERE 조건값 





---

로드

python manage.py loaddata musics/dummy.json

덤핑

python manage.py dumpdata articles > dummy.json --indent 2



---

객체는?

사물을 그대로 가져오기위해 사용

자신의 고유값(주어)

자신이 하는 기능(메소드)(동사)

---





