# if문
# 프로그래밍에서 조건을 판단하여 해당 조건에 맞는 상황을 수행하기 위해 쓰는 것이다.(참과 거짓을 판단하는 문장)
# if와 else의 기본구조
a = True
if a:
    print(1)
else:
    print(2)
# 조건문이 참일 때 1를 출력하고, 거짓일 때 2를 출력함.(else는 if 없이 단독으로 사용이 불가능 함.)
# 들여쓰기
a = False
if a:
    print("수행할문자1")
    print("수행할문자2")
# if문을 만들 때 수행 할 문장을 들여쓰기 해야 한다.
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
# 공백 들여쓰기는 tab이나 space bar로 공백을 주어도 상관없다.(조건문에 콜론(:)은 파이썬의 문법 구조이다.)
# 예시
apple = True
if apple:
    print("사과를 먹어라")
else:
    print("사과를 먹지마")
# apple 값이 참이기 때문에 사과를 먹어라 라는 문구가 출력 됨

# 비교연산자
a = 1
b = 2
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)
# 예시
coin = 10
if coin >= 20:
    print("뽑기를 해라")
else : 
    print("다른걸해라")
# coin의 값이 거짓이기 때문에 다른걸해라 라는 문구가 출력 됨

# or,and,not 연산자
a = True
b = False
print(a or b)
print(a and b)
print(not b)
# 예시
coin = 10
money = True
if coin >= 20 or money:
    print("뽑기를 해라")
else : 
    print("다른걸해라")
# money가 참이고 or은 하나의 값만 참이어도 참을 나타내기 때문에 뽑기를 해라 라는 문구가 출력 됨

# in, not in
# 조건 안에 특정 값이 있는지 없는지 참과 거짓으로 판단함
1 in [1,2,3] # 리스트
1 not in [1,2,3]
'a' in ('a','b','c') # 튜플
'a' not in 'apple' # 문자열
# 예시
home = ['com','tv','table']
if 'tv' in home :
    print('집에서 놀아라')
else:
    print('밖에서 놀아라')
# home 안에 tv라는 값이 있기 때문에 참으로 집에서 놀아라 라는 문구가 출력 됨

# elif
# 다중 조건 판단이 필요 할 떄 쓰인다.
'''if 조건문 :
    수행할 문자
elif 조건문:
    수행할 문자
else:
    수행할 문자'''
# 예시
home = ['come','tv']
ball = True
if 'table' in home:
    print('집에서 놀아라')
elif ball :
    print('밖에서 놀아라')
else : 
    print('그냥 자라')
# if 조건이 거짓일 때 elif로 다른 조건을 주고 조건에 참이었기 때문에 밖에서 놀아라 라는 문구가 출력 됨(elif는 개수 제한없이 쓸 수 있다)
# if 문 한줄 출력
home = ['com','tv','table']
if 'com' in home:
     pass 
else:
    print("밖에서 놀아라")
# 더 간단하게
if 'com' in home : pass
else : print("밖에서 놀아라")
# 수행할 문장을 콜론(:) 뒤에 바로 입력하여 한줄로 출력한다.

# 조건부 표현식
a = 70
if (a >= 60)  :
    b = "good"
else :
    b = "bad" 
print(b)