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