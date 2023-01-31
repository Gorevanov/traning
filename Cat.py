class cat():
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

class Dog(cat):
    def get_pet(self):
        return f'{self.get_name()} {self.get_age()}'

Dog1=Dog("Tok", "boy", 4)

print(Dog1.get_pet())