#while문 처음으로 돌아가기(continue문)
a = 0
while a < 10: # a가 10보다 작은 동안 계속 반복
     a = a + 1 # a 가 1씩 증가한다.
     if a % 2 == 0: continue # a를 나누었을 때 나머지 값이 0이 나올 경우 while문 처음으로 돌아간다.
     print(a) # 9까지 뽑아낸후 while문을 벗어난다.