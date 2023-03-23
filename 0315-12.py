# for문과 range를 이용한 구구단
for a in range(2,10): # a에 2~9의 값을 넣는다
    for b in range(1,10): # b에 1~9의 값을 넣는다
        print(a*b, end=" ") # a와 b의 곱한 값을 한줄에 띄어쓰기 한번씩 해서 출력한다
    print('') # 위 작업이 끝난 후 줄을 바꿔준다.