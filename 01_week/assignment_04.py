a = 5

for i in range(0,a):
    num = int(abs((a-1)/2-i))
    for j in range(0,num):
        print(0, end=" ")
    for k in range(num,a-num):
        print(1, end=" ")
    for z in range(0,num):
        print(0, end=" ")
    print(" ")
