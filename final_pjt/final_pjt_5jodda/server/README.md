# Project 10

## 협업 설정

- Members

  - 오재석
  - 조동빈

- 협업 방식

  Github Flow, Pull & Push Scenario

  - 조동빈: Maintainer
  - 오재석: Maintainer

  Conflict 최소화를 위해 파일 별 작업 분할

- 구현 포인트

  - 기본
    - 샘플 영화 정보
    - accounts
    - movies
    - 장르는 M:N으로
  - 부가
    - 회원 가입 시 선호 장르 선택

<br>

<br>

## 프로젝트 설계

### Roles

- 오재석
  - Seed data parsing
  - Authentication
- 조동빈
  - Movie pages

<br>

### Rules

- Branch를 merge하기 전, 상대방이 gitlab의 discussion을 open하고 close하는 과정을 거친다.

<br>

### Data

이전 프로젝트들에서 사용하던 영화 데이터들 중, 다음 속성들을 갖는 데이터만을 사용

- 영화 번호
- 영화명
- 영화명(영문)
- 시청 연령
- 개봉일
- 장르

1. 영화명(영문)을 제외하고는 Not Null
2. Null 값의 속성이 존재하는 영화 데이터는 DB에 저장하지 않음
3. 장르와 영화는 M:N 관계

<br>





