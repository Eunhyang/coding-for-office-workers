def mul():
     try:
        num = int(input('2에서 9사이의 숫자만 입력해주세요'))
        if 1 < num < 10:
            for i in range(1,10):
                print('{} * {} = {}'.format(num,i,num*i))
        else:
            mul();
     except ValueError as e:
         print(e)

mul()
