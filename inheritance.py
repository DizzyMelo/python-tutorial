class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printName(self):
        print(self.fname, self.lname)


x = Person('Daniel', 'Melo')

x.printName()


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
        # Person.__init__(self, fname, lname)
        # self.fname = fname
        # self.lname = lname

    def welcome(self):
        print('Welcome,', self.fname, self.lname,
              'to the class of', self.graduationyear)


student = Student('Jeff', 'Bezzos', 2020)
student.welcome()
