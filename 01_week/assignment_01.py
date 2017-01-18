import random

kor = ['김밥천국','미미네떡볶이','명동칼국수']
jap = ['규카츠','돈부리','나베']
chi = ['짬뽕타운','양꼬치']


num = input('한식, 중식, 일식 중 한 가지를 골라주세요.')
if num == '한식':
    sel = random.choice(kor)
elif num == '중식':
    sel = random.choice(chi)
elif num == '일식':
    sel = random.choice(jap)
else:
    print("한식,중식,일식 중 선택해야 합니다.")


if sel:
    print('{}중 {}를 선택하셨습니다'.format(num,sel))
