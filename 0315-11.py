a = [90, 20, 70, 40, 50]

for b in range(len(a)): # b 안에 len의 range값을 순서대로 넣어준다
    if a[b] < 60: 
        continue
    print("%d번 학생 합격입니다." % (b+1)) # 60 보다 값이 큰 학생은 거짓으로 continue를 하지않고 바로 출력된다.