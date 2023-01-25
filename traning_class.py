class car():
    """Описание автомобиля"""
    def __init__(self, model, model1, year):
        """свойства автомобиля"""
        self.model = model
        self.year = year
        self.model1 = model1
        self.market = "автомобиль продается"
    def description_car (self):
        print(" Автомобиль " + self.model +" "+ self.model1,  " выпущен в " + str(self.year) + " году.")
        return("")
car1 = car("Lada", "семерка", 2011)
car2 = car("Opel", "astra", 2018)
car3 = car("toyota", "land cruser", 2001)

car1.description_car()

print(car3.market)
print()


class Human:
    age = None

    def __init__(self, age=4):
        self.age = age

    # добавляем геттер - специальный метод для получения поля
    def get_age(self):
        return self.age

    # добавляем сеттер - специальный метод для установки нового значения
    def set_age(self, age):
        if age > 0 and isinstance(age,
                                  int):  # проверяем условия, что человеку должно быть больше 0 лет и его возраст - целое число
            self.age = age


h = Human()
h.set_age(0)
print(h.get_age())