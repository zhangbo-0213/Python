class Person:
    def test(self,name,age):
        self.name=name
        self.age=age
        self.grade=1
        print('name:{} age:{} grade:{}'.format(self.name,self.age,self.grade))

    def test2(self):
        self.grade=2
        print('name:{} age:{} grade:{}'.format(self.name,self.age,self.grade))

p=Person()
p.test('bo',23)
p.test2()
