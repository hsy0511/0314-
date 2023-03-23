# while문 강제로 빠져 나가기 break문
candy = 5
coin = 500
while coin: # coin은 500을 가지고 있어 참으로 표현되고 무한 반복이 된다.
    print("100원 받았습니다. 사탕 여기요")
    candy = candy-1 # candy를 1씩 감소시킨다
    print("남은 사탕은 %d개 입니다." %candy)
    if candy == 0 :
        print("사탕이 없습니다. 판매중지 합니다.")
        break# candy가 0이되면 프린트 하고 break문이 호출되어 while문을 빠져 나간다.