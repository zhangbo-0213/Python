class MyClass:
    name='Sam'
    def SayHi(self):
        print 'Hello {} {}'.format(self.name,self.name)

class SchoolMember:

    def __init__(self,name,age):
        self.name=name
        self.age=age

        print('(Initialized SchoolMember:{}{})'.format(self.name,self.age))

    def tell(self):
        self.doc='This is ParentClass'
        print('Name:"{}" Age:"{}" {}'.format(self.name,self.age,self.doc)),

class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print('(Initialized Teacher:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:"{:d}"'.format(self.salary))

class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks=marks
        print('(Initialized Student:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:"{:d}"'.format(self.marks))

t=Teacher('Tom',25,3000)
s=Student('Major',23,97)
print
members=[t,s]
for m in members:
    m.tell()
