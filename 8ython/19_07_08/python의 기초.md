# python의 기초



## 자료형

### 변수 (value)

하나의 값만 저장

박스 하나

```python
a = 60
a = "60"
```





### 리스트(list)

번호에 각 값을 저장 0부터 사용

연결된 박스

``` python
a= [1, 2, 3]
```





### 딕션어리 (dictionary)

견출지가 붙은 박스

```python
dust = {"강남구": 58}
```





### if(조건문)

```python
if 조건문1:
    조건문1이 참일때 실행
elif 조건문2:
    조건문1이 거짓이고 조건문2가 참일때 실행
else:
    조건문이 다 거짓이면 실행

```

- elif와 else는 0~번 사용가능



### 반복문 for / while

```python
for i in 반복할 변수를 모은 것:
    반복할 변수를 모은 것 내에서 차래로 한 번씩 적용
    
while 반복조건:
    반복 조건이 참일때 실행문
    
```



* for문에서는 list, 튜플, dict, set모두 가능하다.



### random

```python
import random

numbers = range(1,46)
print(random.sample(numbers,6))

```



### 유용한 내장함수

``` python
sorted()	# 내림차순
range()		# 수열
input()		# 입력값을 받음
```



