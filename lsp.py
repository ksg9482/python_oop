# LSP(Liskov Substitusion Principle)
from abc import *


class SmartPhone:
    type: str = "base_phone"

    def call(self):
        print("Calling")
    
    def send_message(self):
        print("Sending a message")

    def internet(self):
        print("Surfing the internet")

    def app_store(self):
        print("Opening the app store")

class Galaxy(SmartPhone):
    type: str = "Galaxy"
    
    def app_store(self):
        print("Opening Galaxy Store")

class Character(metaclass=ABCMeta):
    def __init__(self, name='yourname', health_point=100, striking_power=3, defensive_power=3):
        self.name = name
        self.health_point = health_point
        self.striking_power = striking_power
        self.defensive_power = defensive_power        
    
    def get_info(self):
        print (self.name, self.health_point, self.striking_power, self.defensive_power)
    
    @abstractmethod
    def attack(self, second):
        pass

    @abstractmethod
    def receive(self):
        pass

    @abstractmethod
    def special(self):
        pass