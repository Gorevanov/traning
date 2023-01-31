class Customers:
    def __init__(self, name1, name2, city, balance):
        self.name1=name1
        self.name2=name2
        self.city=city
        self.balance=balance
    def __str__(self):
        return f"{self.name1} {self.name2}. {self.city}. Баланс:{self.balance} руб."

    def get_gest(self):
        return f"{self.name2} {self.city}."

Cust1=Customers('Виктор', 'Грозный', 'Москва', 6500)
Cust2=Customers('Марина', 'Галкина', 'Москва', 6400)
Cust3=Customers('Жора', 'Петькин', 'Москва', 2000)
Cust4=Customers('Петя', 'Мул', 'Москва', 7500)

gust_list=[Cust1,Cust2,Cust3,Cust4]


for gust in gust_list:
    print(gust.get_gest())

