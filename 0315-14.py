# 리스트 컴프리헨션을 통해 구구단 작성
a = [b*c for b in range(2,10)
    for c in range(1,10)]
print(a) # a 리스트 안에 2개에 for문을 사용하여 구구단을 출력할 수 있다.