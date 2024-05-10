# OCP(Open Closed Principle)
# 확장에는 열려있고 수정에는 닫혀있어야 한다.

class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
class Circle:
    def __init__(self, radius):
        self.radius = radius

class AreaCalculator(object):
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.width * shape.height
        return total

# 도형이 추가될 때마다 AreaCalculator를 수정해야 함
# Circle은 width, height가 없고 radius만 있음
shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area())

# 객체 자신이 자신의 데이터에 대한 로직을 가지고 있음
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
    
# 도형이 추가되어도 변경 없음
# 도형 자신이 자신의 면적을 계산하므로 AreaCalculator는 단순히 더하기만 함
class AreaCalculator(object):
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area()
        return total


shapes = [Rectangle(1, 6), Rectangle(2, 3), Circle(5), Circle(7)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area())