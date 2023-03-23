# for문과 continue
a =[90,20,50,70,30]

b = 0
for c in a : # c값에 a리스트에 첫번째 값부터 마지막 값까지 넣어줍니다
    b = b+1 # for문이 한번씩 돌아갈때 마다 b는 1씩 증가합니다.
    if c < 60: 
        continue
    print("%d번째 학생 합격입니다." %b) # c 보다 값이 큰 학생은 거짓으로 continue를 하지않고 바로 출력된다.