class User:
    def __init__(self,name,age,gender,position):
        self.name = name
        self.age = age
        self.gender = gender
        self.position = position

class Partner(User):
    position = '대리'

name = input('이름을 입력하세요')
age = input('나이를 입력하세요')
gender = input('성별을 입력하세요')
position = input('직급을 입력하세요')
a = User(name,age,gender,position)
print(a.__dict__)
