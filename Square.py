class Square:
    _a=None
    def __init__(self, a):
        self.a=a
    @property
    def a (self):
        return self._a
    @a.setter
    def a(self, valeo):
       if valeo>0:
           self._a=valeo
    @property
    def area(self):
        return self.a**2

Square1=Square(25)

print(Square1.area)