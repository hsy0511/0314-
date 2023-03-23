# for문과 함께 자주 사용하는 range 함수
# range 함수는 range(1, 11)으로 설정하면 1~10까지 지정해주는 함수이다.(range(10)을 하면 (0,10)이 된다.)
# range 함수 예시

a=0
for b in range(1,11): # b에 range로 불러드린 1~10값을 더한 값을 넣어준다.
    a = a+b
    
print(a) # for문 밖에서 출력해준다.