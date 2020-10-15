class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y

    def get(self):
        return self.x, self.y

    def move(self, offsetx, offsety):
        self.x += offsetx
        self.y += offsety

    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
        
    ## x + y ==> (2, 3) + (2, 2) => (4, 5)
    ## x + 8 ==> (2, 3) + 8 ==> (10, 11)
    def __add__(self, other):
        if type(other) == Point:
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)


# linha de comando:
'''
p = Point()
p

p = Point(1,2)
p

q = Point(3,4)
q

p + q

p+2

'''
