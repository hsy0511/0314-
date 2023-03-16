# 0315-파이썬
# if문
### 프로그래밍에서 조건을 판단하여 해당 조건에 맞는 상황을 수행하기 위해 쓰는 것이다.(참과 거짓을 판단하는 문장)
## if와 else의 기본구조
```python
a = True
if a:
    print(1)
else:
    print(2)
```
### 조건문이 참일 때 1를 출력하고, 거짓일 때 2를 출력함.(else는 if 없이 단독으로 사용이 불가능 함.)
## 들여쓰기
```python
a = False
if a:
    print("수행할문자1")
    print("수행할문자2")
'''
a = True
if a:
    print("사과를")
print("먹어라")
    print("!!!")
오류가 발생함

a = True
if a:
    print("사과를")
    print("먹어라")
        print("!!!")
오류가 발생함

'''
```
### if문을 만들 때 수행 할 문장을 들여쓰기 해야 한다.
### 공백 들여쓰기는 tab이나 space bar로 공백을 주어도 상관없다.(조건문에 콜론(:)은 파이썬의 문법 구조이다.)
### 예시
```python
apple = True
if apple:
    print("사과를 먹어라")
else:
    print("사과를 먹지마")
# apple 값이 참이기 때문에 사과를 먹어라 라는 문구가 출력 됨
```
## 비교 연산자
```python
a = 1
b = 2
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)
```
### 예시
```python
coin = 10
if coin >= 20:
    print("뽑기를 해라")
else : 
    print("다른걸해라")
# coin의 값이 거짓이기 때문에 다른걸해라 라는 문구가 출력 됨
```
## or,and,not 연산자
```python
a = True
b = False
print(a or b)
print(a and b)
print(not b)
```
## 예시
```python
coin = 10
money = True
if coin >= 20 or money:
    print("뽑기를 해라")
else : 
    print("다른걸해라")
# money가 참이고 or은 하나의 값만 참이어도 참을 나타내기 때문에 뽑기를 해라 라는 문구가 출력 됨
```
## in, not in 연산자
### 조건 안에 특정 값이 있는지 없는지 참과 거짓으로 판단함
```python
1 in [1,2,3] # 리스트
1 not in [1,2,3]
'a' in ('a','b','c') # 튜플
'a' not in 'apple' # 문자열
```
## 예시
```python
home = ['com','tv','table']
if 'tv' in home :
    print('집에서 놀아라')
else:
    print('밖에서 놀아라')
# home 안에 tv라는 값이 있기 때문에 참으로 집에서 놀아라 라는 문구가 출력 됨
```
## elif
### 다중 조건 판단이 필요 할 떄 쓰인다.
```python
'''if 조건문 :
    수행할 문자
elif 조건문:
    수행할 문자
else:
    수행할 문자'''
```
### 예시
```python
home = ['come','tv']
ball = True
if 'table' in home:
    print('집에서 놀아라')
elif ball :
    print('밖에서 놀아라')
else : 
    print('그냥 자라')
# if 조건이 거짓일 때 elif로 다른 조건을 주고 조건에 참이었기 때문에 밖에서 놀아라 라는 문구가 출력 됨(elif는 개수 제한없이 쓸 수 
```
## if 문 한줄 출력
```python
home = ['com','tv','table']
if 'com' in home:
     pass 
else:
    print("밖에서 놀아라")
# 더 간단하게
if 'com' in home : pass
else : print("밖에서 놀아라")
# 수행할 문장을 콜론(:) 뒤에 바로 입력하여 한줄로 출력한다.
```
## 조건부 표현식
```python
a = 70
if a >= 60:
    b = "good"
else :
    b = "bad" 
print(b)
```
# while문
### 반복하여 문장을 수행하기 위해 사용하는 것이다.
## while문에 기본구조
```python
''
while 조건문:
    수행할 문장
    수행할 문장
'''
# while문은 값이 거짓일 때까지 문장들을 계속 반복 시킨다.
```
### 예시
```python
a = 0
while a < 3: # a가 3보다 작은 동안 계속해서 반복한다.
    a = a+1 # a 값이 1씩 증가한다.
    print("사탕 %d개 먹었습니다" %a) 
    if a == 3 : 
        print("충치 생겼습니다") # a와 3이 같은 값이면 프린트한다.
```
## while문 만들기
```python
a = """ 
1. one
2. two
3. three
4. four

숫자입력:""" # a 문자열
b = 0 # 변수 b를 0으로 설정
while b != 4: # b는 4와 같이 않다는 조건을 실행
    print(a) 
    b = int(input()) # int(input())로 숫자를 입력받게 한다. 4를 입력하면 거짓이 되므로 while문을 빠져나간다.
```
## while문 강제로 빠져나오기 (break문)
```python
candy = 5
coin = 500
while coin: # coin은 500을 가지고 있어 참으로 표현되고 무한 반복이 된다.
    print("100원 받았습니다. 사탕 여기요")
    candy = candy-1 # candy를 1씩 감소시킨다
    print("남은 사탕은 %d개 입니다." %candy)
    if candy == 0 :
        print("사탕이 없습니다. 판매중지 합니다.")
        break# candy가 0이되면 프린트 하고 break문이 호출되어 while문을 빠져 나간다.
```
## break문 input
```python
candy = 5 # 변수 candy를 5로 지정
while True:
    coin = int(input("동전을 넣어주세요:")) # 입력받은 숫자를 coin 변수에 대입하는것
    if coin == 200:
        print("사탕나왔습니다.")
        candy = candy-1 # coin이 200이면 candy를 하나 감소 시키고 사탕을 줍니다를 출력 
    elif coin>200:
        print("사탕이랑 거스름돈 %d원 나왔습니다 " % (coin -200))
        candy = candy -1 # coin이 200 보다 많이 들어오면 coin -200dml 의 값을 돌려주고 candy는 1씩 감소한다.
    else:
        print("돈을 돌려주고 사탕을 주지 않습니다.")
        print("사탕이 %d개 남았습니다."%candy) # 그 밖에 값을 넣으면 프린트하고 candy의 남은 값을 출력
    if candy==0:
        print("남은 사탕이 없습니다. 판매중지 합니다.")
        break # candy가 0이 되면 프린트하고 break문으로 while문을 벗어난다.
```
## while문 처음으로 돌아가기(continue문)
```python
a = 0
while a < 10: # a가 10보다 작은 동안 계속 반복
     a = a + 1 # a 가 1씩 증가한다.
     if a % 2 == 0: continue # a를 나누었을 때 나머지 값이 0이 나올 경우 while문 처음으로 돌아간다.
     print(a) # 9까지 뽑아낸후 while문을 벗어난다.
```
## 무한 루프
```python
while True:
    print("shift+f5를 눌러서 while문을 벗어나기")
    # while문의 조건이 참이기 때문에 무한 루프로 돌아간다.(shift+f5는 반복문을 종료하는 키이다)
```
# for문
## for문 기본구조
```python
'''
for 변수 in 리스트 또는 튜플, 문자열:
수행할 문자
'''
a = ['q','w','e','r']
for b in a: # 리스트 첫번째 값이 b 변수에 먼저 대입된 후 마지막 까지 대입하여 출력하는것
    print(b)

a =[(1,2),(3,4),(5,6)]
for (first,last) in a: # a리스트 요소값이 튜플 이기 때문에 각각의 요소가 자동으로 변수에 대입된다
    print((first+last)) # 출력을 할 때는 튜플에 첫번째 요소와 마지막 요소를 더해서 출력한다
```
## for문 응용예시
```python
a =[90,20,50,70,30]
b = 0
for c in a : # c값에 a리스트에 첫번째 값부터 마지막 값까지 넣어줍니다
    b = b+1 # for문이 한번씩 돌아갈때 마다 b는 1씩 증가합니다.
    if c >=60: 
        print("%d번 학생은 합격입니다"%b)
    else:
        print("%d번 학생은 불 합격입니다."%b) # c가 60보다 같거나 크면 합격을 나타내고 나머지는 불합격을 나타냄
```
## for문과 continue
```python
a =[90,20,50,70,30]

b = 0
for c in a : # c값에 a리스트에 첫번째 값부터 마지막 값까지 넣어줍니다
    b = b+1 # for문이 한번씩 돌아갈때 마다 b는 1씩 증가합니다.
    if c < 60: 
        continue
    print("%d번째 학생 합격입니다." %b) # c 보다 값이 큰 학생은 거짓으로 continue를 하지않고 바로 출력된다.
```
## for문과 함께 자주 사용되는 range 함수
### 함수는 range(1, 11)으로 설정하면 1~10까지 지정해주는 함수이다.(range(10)을 하면 (0,10)이 된다.)
### 예시
```python
a=0
for b in range(1,11): # b에 range로 불러드린 1~10값을 더한 값을 넣어준다.
    a = a+b
    
print(a) # for문 밖에서 출력해준다.

a = [90, 20, 70, 40, 50]

for b in range(len(a)): # b 안에 len의 range값을 순서대로 넣어준다
    if a[b] < 60: 
        continue
    print("%d번 학생 합격입니다." % (b+1)) # 60 보다 값이 큰 학생은 거짓으로 continue를 하지않고 바로 출력된다.
    
```
## for문과 range를 이용한 구구단
```python
# for문과 range를 이용한 구구단
for a in range(2,10): # a에 2~9의 값을 넣는다
    for b in range(1,10): # b에 1~9의 값을 넣는다
        print(a*b, end=" ") # a와 b의 곱한 값을 한줄에 띄어쓰기 한번씩 해서 출력한다
    print('') # 위 작업이 끝난 후 줄을 바꿔준다.
```
## 리스트 컴프리헨션 사용하기 
### 리스트 컴프리헨션을 사용하면 좀 더 편리하고 직관적인 프로그램을 만들 수 있다.
### 예제 1
```python
a = [1,2,3,4]
b=[]
for c in a:
    b.append(c*3)
print(b)
# 예제 1번을 리스트 컴프리헨션하게 되면 이렇게 된다.
a = [1,2,3,4]
b = [c*3 for c in a] # b리스트 안에서 for문을 진행하게 된다.
print(b)
```
## 예제 2
```python
a = [1,2,3,4]
b = [c*3 for c in a if c%2==0] # b리스트 안에서 for문과 if문을 진행하게 된다.
print(b)
```
## 리스트 컴프리헨션을 사용하여 구구단 작성
```python
a = [b*c for b in range(2,10)
    for c in range(1,10)]
print(a) # a 리스트 안에 2개에 for문을 사용하여 구구단을 출력할 수 있다.
```
# Quiz
```python
# Quiz
from random import *
a = list(range(1,51))
b = sample(list(range(5,51)),1)
x = a[0]
y = b[0]


x = 0
for y in list(range(1,51)) :
    z = sample(range(5,51),1)
    if 5<=z[0]<=15 :
        print("[o]{0}번째 손님 (소요시간 : {1}분".format(y,z[0]))
        x=x+1
    elif x == 15:
        print("[]{0}번째 손님 (소요시간 : {1}분".format(y,z[0]))
    else:
        print("[]{0}번째 손님 (소요시간 : {1}분".format(y,z[0]))

print(sum(z),end="명")     
```
### 결과
![image](https://user-images.githubusercontent.com/104752580/225229763-236a84f3-3eda-4da5-b032-28bc35129703.png)
