class User:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

class Partner(User):
    def __init__(self,name,age,gender,position):
        super().__init__(name,age,gender)
        self.position = position

b = Partner('Jason','24','Male','대리')
print(b.__dict__)
