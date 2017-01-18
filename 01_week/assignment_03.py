import random

ROCK = '바위'
SCISSORS = '가위'
PAPER = '보'

RCP_LIST = (
    ROCK,
    SCISSORS,
    PAPER
)
# print('당신은 ' + you + ', 저는 ' + me + '이므로')

win = 0
loose = 0

while win<3 and loose<3 :
    you = input('{}, {}, {}? '.format(SCISSORS,ROCK,PAPER))
    me = random.choice(RCP_LIST)
    if you == me:
        print('동점!')
    elif ((you == SCISSORS and me == ROCK) or
          (you == ROCK and me == PAPER) or
          (you == PAPER and me == SCISSORS)) :
                print('당신은 {}, 저는 {}이므로 제가 이겼습니다!'.format(you,me))
                loose = loose + 1
    elif you not in RCP_LIST:
        print('가위,바위,보 중 선택하세요.')
    else:
        print('당신은 {}, 저는 {}이므로 당신이 이겼습니다!'.format(you,me))
        win = win + 1


print('최종스코어는 승: {}, 패 {} 입니다.'.format(win,loose))
