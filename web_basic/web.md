# web

### 서비스의 구조

서비스의 구조는 항상 요청(request)과 응답(response)으로 이뤄 진다.



### web server

일반적으로 서버 컴퓨터를 생각하지만

사실 요청을 처리하여 응답하는 프로그램을 만드는 것이다.



### 요청의 종류

1. 줘라 (Get)

2. 받아라 (Post)



### web의 종류

1. Static Web
2. Dynamic Web



### URL

통합 자원 식별자

남의 서버에 요청을 보내 처리하는 방식

컴퓨터 주소인 IP주소를 이용해 각 문서에 접근한다!



# HTML

## What is HTML?

HTML = Hyper Text Markup Language

이제 이 단어를 쪼개보자!



### Hyper Text

기존의 택스트는 문서의 연결이 비교적 단순했다. 즉 각주/미주를 달면 해당하는 문서로 가는 방식으로 정리가 된다. 즉 단방향 적으로 참조를 하게 구성되어있다.

하지만 하이퍼 택스트(Hyper Text)는 이런 단방향적인 참조에서 벗어나 다수의 문서들이 링크를 통해 서로의 또는 문서 자신의 특정 위치로 참조를 하게 된다. 이런 방식은 문서간의 복잡도가 증가하지만 정보의 표시나 연결에 보다 효과적이다. 이런 방식을 하이퍼 택스트라고 한다.

이런 하이퍼 택스트를 주고받는 방식을 규정한 것이 바로 Hyper Text Transfer Protocol 즉 http이다.

하지만 http는 단순한 정보 전달을 하는 방식으로 보안이 부족하고, 속도가 느리다는 단점이 있는데 이를 보안한 (높은 보안성과 빠른 속도를 가진) https로 전환이 일어나고 있다.

해쉬테그를 이용한 https는 정보의 은닉성과 속도를 크게 높이게 되는데 이는 http://httpvshttps.com,https://httpvshttps.com에서 시각적으로 볼 수 있다.



### Markup

하나의 글꼴을 가진 줄글로 된 문서가 존재한다고 하면 이 문서는 가독성이 크게 떨어진다. 그래서 형식이 지정되는데 그중 웹에서 사용하는 스타일이 바로 마크업 스타일이다.

일반적으로는 마크다운과 유사 하다.



### Language

브라우저가 html을 해석하여 하나 웹 페이지를 구성하기 위해서는 마크업으로는 표현에 한계가 존재한다. 그래서 이를 보조할 다양한 테그들이 존재한다.

테크는 많으므로 따로 정리하겠다.



### HTML 구조

DOCTYPE선언부

html 요소

​	사용언어 설정



### DOM tree 구조

html의 구조는 기본적으로 DOM(document object model) tree 구조이다.

tree: 계층 관계가 있는 순환이 없는 단방향 그래프  root에서 경로 길이 만큼의 값을 계층으로 본다.

경로가 있으면 부모 자식관계라고 부른다

같은 부모 아래의 자식은 sibling이라고 한다.



주석 <!-- 내용 -->

<h1>큰 제목</h1>



<img src='url'/>



non semantic 테그

div테그

display:block을 지정하기 위한 기본 레이아웃 태그

span



semantic 테그

header 문서 전체나 섹션의 헤더(제일 위에 있는 것)





**seo 검색 엔진 최적화**