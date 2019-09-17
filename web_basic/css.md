# CSS

## freeview

emmet : html 자동완성기능 관련 문서

table>tr\*(줄 수)>td\*(열 수)

### input 정리

type : input의 형식

1.  text
2. date
3. datetime
4. redio
5. checkbox

name : action에 테그 하는 것

placeholder : 사라지는 글자

value : 초기값



### select

내부에 option 테그를 통해 여러가지 체크 리스트를 보여준다



### 기타 

span테그 : 줄을 감싸주는 느낌 테그로 시작하지 않을때 사용

br테그 : 줄바꿈 테그



### 글꼴

noto sans : 표준 글꼴



## 본수업

## 경로

절대경로 : 특정 폴더 또는 root 폴더에서 접근

상대경로 : working dir에서접근

../ : 상위 폴더



## CSS

html으로 잡은 벼대에 styling 하는 것

html와 css은 별개의 언어



### 기본 용법

bg : #f0f0f0

text: #3b3a30



inline styling : 코드에 적용

tag styling : 테그 전체에 적용

link로 외부 파일을 불러 올 수 있다.(link 탭)



### box model

html문서를 작성하면 각 테그는 4단 박스로 되어있다. 바깥부터 마진(margin), 보더(border), 페딩(padding), 컨텐츠(content)로 구성된다. 이 4가지가 상호작용하며 스타일링이 된다.

실제 가장 많이 쓰이는 CSS 문법이 이런 각 박스의 여백을 조정하는 것이다.

스테틱한 블록의 margin은 서로 공유한다 (마진 컬랙팅)

각 박스의 스타일링 지정은 4방향으로 다르게 지정 할 수 있다. 이때 표시 속성에 따른 적용범위는 다음과 같다.

1. all 

2. (t b) (r l) / (top bottom) (right left)

3. t (r l) b / top (right left) bottom

4. t b r l / top bootom right left

여러가지 스타일링을 묶음으로 표현할 수 있으나 이 때는 전체 조정만 가능하다.



## display

block, inline, block-inline, flex 등의 형식으로 표현이 가능하다.

### block

마진으로 정렬 할 수 있다.

### inline

마진 등등 이 제한된다

span a input select textarea button br img strong i ---암기하자

### inline-block

inline의 특성을 가지고 각 박스의 조절이 가능하다.

###  flex

나중에 할 예정



## Class/Id

특정 스타일을 적용하는 묶음으로 함수와 유사한 개념을 가지는 class와 id는 여러가지 형식의 스타일을 한 번에 적용 할 수 있다.

### class

대체로 다수의 개체에 같은 스타일을 적용 할 때 사용한다. 적용은 테그내에서 class="클레스1 클래스2..."

단축키는 .클래스명

### id

대체로 하나의 개체에 같은 스타일을 적용 할 때 사용한다. 적용은 태그내 id="id명"

단축키는 #id명









## visibility

개체를 보이게하는 visible와 안보이는 hidden을 설정 가능하다.



## Position

### static (기본 위치)

아무 설정을 하지 않았을 때의 값 위에서부터 블록이 스테틱하게 들어간다.

### relative (상대위치)

static 위치에서 움직인다. 방향은 top, bottom, left, right

### absolute (절대 위치)

가장 가까운 조상의 content좌상단을 기준으로 이동 자손의 margin의 좌상단이 기준이다.

### fixed

보이는 창을 기준으로 좌표를 설정

### z-index

각 블록의 위치 지정 디폴트는 0 같은 레벨일 떄는 html 문서 위치상 아래에 있는 것이 위에 있다.
