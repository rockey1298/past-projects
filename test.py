class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        print(f"{self.name}{self.age}{self.color}")


D = Dog("Michael", 13, "orange")
D.speak()
