# ISP(Interface Segregation Principle) 인터페이스 분리 원칙
from abc import *

"""
클래스를 만들기 위해 파이썬에서는 기본 metaclass가 사용됨
* 즉, 클래스를 만들기 위해서 메타클래스 라는 것이 필요
* class 생성시, () 아무 것도 넣지 않으면, 기본 파이썬에서 클래스를 만들기 위한 메타클래스가 쓰인다
"""

class Character(metaclass=ABCMeta):
    @abstractmethod
    def attack(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class Elf(Character):
    def attack(self):
        print ("practice the black art")
    
    def move(self):
        print ("fly")
        
class Human(Character):
    def attack(self):
        print ("plunge a knife")
    
    def move(self):
        print ("run")

    def eat(self):  # <--- 메서드 확장
        print ("eat foods")


# 공격 수단을 추상클래스로 만들고 각 클래스에서 상속받아 사용
# 마찬가지로 방어타입이나 필요한 것도 클래스 조합으로 만들어 사용 가능
class UsingKnife(metaclass=ABCMeta):
    @abstractmethod
    def use_knife(self):
        pass

class UsingWizard(metaclass=ABCMeta):
    @abstractmethod
    def use_wizard(self):
        pass

class Warrior(UsingKnife):
    def use_knife(self):
        print ('칼로 찌른다')

class Elf(UsingWizard):
    def use_wizard(self):
        print ('마법을 쓰다')

class Wizard(UsingWizard):
    def use_wizard(self):
        print ('마법을 쓰다')

warrior1 = Warrior()
elf1 = Elf()
wizard1 = Wizard()

warrior1.use_knife()