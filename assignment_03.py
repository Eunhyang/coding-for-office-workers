import random

rpc = ['가위','바위','보']

you = input('가위?바위?보?')
me = random.choice(rpc)
print('당신은 ' + you + ', 저는 ' + me + '이므로')

if you == me:
    print('동점!')
else:
    if you == rpc[0]:
        if me == rpc[1]:
            print('제가 이겼습니다!')
        else:
            print('당신이 이겼습니다!')
    elif you == rpc[1]:
        if me == rpc[2]:
            print('제가 이겼습니다!')
        else:
            print('당신이 이겼습니다!')
    else :
        if me == rpc[0]:
            print('제가 이겼습니다!')
        else:
            print('당신이 이겼습니다!')
