class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("Bark")


class Cat(Mammal):
    def meow(self):
        print("Meow")


cat = Cat()
cat.meow()
cat.walk()

dog = Dog()
dog.bark()
dog.walk()