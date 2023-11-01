class Vektor2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def lenght(self):
        return (self.x**2 + self.y**2)**0.5
    def add(self, other):
        self.x += other.x
        self.y += other.y
    def mul(self, other):
        return self.x*other.x + self.y*other.y
    def prt(self):
        print(self.x, self.y)

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    def prt(self):
        print(self.x, self.y, self.r)
    def area(self):
        return 3.14*self.r**2
    def perimeter(self):
        return 2*3.14*self.r
    def move(self, x, y):
        self.x += x
        self.y += y
    def dist(self, other):
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5

ab = Vektor2D(1, 2)
cd = Vektor2D(3, 4)
scal = ab.mul(cd)

c = Circle(0,0,10)
d = Circle(10,10,5)
print(c.dist(d))