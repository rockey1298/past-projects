class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")

    def speak(self):
        print('I dont know what i say')


class Cat(Pet):
    def __init__(self, name, age, color):
        #super is the class you inherit from, pet class
        super().__init__(name, age)
        self.color = color


    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and i am {self.color}. I am {self.age} years old")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet('Andrew', 23)
p.show()
p.speak()
c = Cat('bill', 34, 'grey')
c.show()
c.speak()
d = Dog('jill', 25)
d.show()
d.speak()
f = Fish("bubbles", 10)
f.show()
f.speak()
