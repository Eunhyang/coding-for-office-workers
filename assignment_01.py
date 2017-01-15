import random

kor = ['김밥천국','미미네떡볶이','명동칼국수']
jap = ['규카츠','돈부리','나베']
chi = ['짬뽕타운','양꼬치']

num = input('1:한식, 2:중식, 3:일식 중 한 가지를 골라주세요.')

if num == 1 :
    print(random.choice(kor))
elif num == 2 :
    print(random.choice(jap))
else:
    print(random.choice(chi))