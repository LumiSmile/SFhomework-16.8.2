class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
baron = Cat(name='Baron', gender='boy',age=2)
sam = Cat(name='Sam', gender='boy', age=2)

print(baron.age)
print(sam.name)