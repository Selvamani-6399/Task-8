class MyClass:
    def __init__(self,x):
        self.pi = x

    def display(self):
        print(f"Value of pi is {self.pi}")

value = MyClass(3.141)
value.display()