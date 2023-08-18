class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()


    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people


    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


def number_of_people(cls):
    return cls.number_of_people


p1 = Person('bob')
p2 = Person('steve')
print(Person.number_of_people_())
