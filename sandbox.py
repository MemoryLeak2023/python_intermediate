class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError('age must be positive')
        self.__age = age

ferry = Person(-10)

print(ferry.age)
ferry.age = 3
print(ferry.age)