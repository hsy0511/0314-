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
    else:
        print("[]{0}번째 손님 (소요시간 : {1}분".format(y,z[0]))


print(x,end="명")     
    
    
    
