from abc import *

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

"""
게임 캐릭터는 다음과 같이 3명이 존재하고, 각각의 메서드는 다음과 같음
Warrior
 - 공격하면 칼로 찌른다를 출력
Elf
 - 공격하면 마법을 쓴다를 출력
Wizard
 - 공격하면 마법을 쓴다를 출력
"""

class BaseUnit():

    def __init__(self, striking_point:int, health_point:int):
        self.striking_point = striking_point
        self.health_point = health_point

    def attack(self, enemy_unit):
        print("attack")

    def receive(self, enemy_striking_point:int):
        damage = enemy_striking_point - self.health_point
        if damage >= self.health_point:
            print("죽었음")
            return "죽었음"
        else:
            self.health_point -= damage

class Warrior(BaseUnit):

    def __init__(self):
        super().__init__(10, 100)

    def attack(self, enemy:BaseUnit):
        print("칼로 찌른다")
        enemy.receive(self.striking_point)

    def use_shield(self):
        print("1번 공격을 막는다")

class Elf(BaseUnit):

    def __init__(self):
        super().__init__(10, 100)

    def attack(self, enemy:BaseUnit):
        print("마법을 쓴다")
        enemy.receive(self.striking_point)

    def wear_manteau(self):
        print("1번 공격을 막는다")

class Wizard(BaseUnit):

    def __init__(self):
        super().__init__(10, 100)

    def attack(self, enemy:BaseUnit):
        print("마법을 쓴다")
        enemy.receive(self.striking_point)

    def use_wizard(self):
        self.health_point += 3
        print("자신의 health_point를 3씩 올려준다")

characters:list[BaseUnit] = [Warrior(), Elf(), Wizard()]
for character in characters:
    character.attack()

