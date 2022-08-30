class ame:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func1(self):
        print('hello, ' + self.name)

    def func2(self):
        print('you are ' + self.age)

p1 = ame("kun", "32")
p1.func1()
p1.func2()
