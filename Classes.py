class Person:

    def __init__(self, name):
        self.name = name
        print(self.name)

    def talk(self):
        print(f"{self.name} is talking")


name = input("Enter The Name Of Person : ")
person = Person(name)
person.talk()
