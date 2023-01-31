class rectangle1:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def get_area(self):
        return self.x * self.y

    def __str__(self):
        return f'rectangle1: {self.x, self.y}'

r1=rectangle1(5,10)
r2=rectangle1(50, 100)

print(r2.get_area())