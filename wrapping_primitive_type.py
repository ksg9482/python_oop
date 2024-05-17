"""
변수를 선언하는 2가지 방법
"""
age = 20 # 1. 원시타입 변수 선언

class Age:
    def __init__(self, age):
        self.age = age
age = Age(20) #2. 원시타입을 객체로 포장해 선언

"""
원시타입을 객체로 포장하면 얻을 수 있는 이점

# 1. 자신의 상태를 객체 스스로 관리할 수 있다.
"""

# 사용자의 나이를 가진 User의 경우 예시
class User:
    def __init__(self, age: int):
        self.age = age

"""
원시 타입인 int로 나이를 가지고 있으면?
우선, 나이에 관한 유효성 검사를 User클래스에서 하게 된다.
"""
class User:
    def __init__(self, input: str):
        age = int(input)
        if age < 0:
            raise ValueError("나이는 0살 부터 시작합니다.")
        self.age = age

"""
지금은 User 클래스의 멤버 변수가 나이 밖에 없지만 이름, 이메일 등 추가적인 값을 관리하게 되면 문제가 생길 수 있다.

두 글자 이상의 이름만 지원한다고 가정하고, 이름 변수 추가
"""

class User:
    def __init__(self, name_value:str, age_value: str):
        age = int(age_value)
        self.validate_name(name_value)
        self.validate_age(age_value)
        self.name = name_value
        self.age = age

    def validate_age(self, age:int) -> None:
        if age < 0:
            raise ValueError("나이는 0살 부터 시작합니다.")
        
    def validate_name(self, name:str) -> None:
        if len(name) < 2:
            raise ValueError("이름은 2글자 이상이어야 합니다.")
        
"""
두 개의 멤버 변수를 선언했을 뿐인데 User클래스가 할 일이 많아졌다.
이름 값에 대한 상태관리, 나이 값에 대한 상태관리를 모두 해야 한다.

User 클래스가 원하는 것은 사용자 그 자체 상태만 관리하는 것이다.
"""

"""
원시 타입 포장
"""
class User:
    def __init__(self, name: str, age: int):
        self.name = Name(name)
        self.age = Age(age)

class Name:
    def __init__(self, name: str):
        if len(name) < 2:
            raise ValueError("이름은 2글자 이상이어야 합니다.")
        self.name = name

class Age:
    def __init__(self, age: int):
        if age < 0:
            raise ValueError("나이는 0살 부터 시작합니다.")
        self.age = age

"""
이름과 나이를 각각 Name, Age가 담당하도록 바뀌었다. 유효성 검증 및 상태값을 스스로 관리할 수 있게 되었다.
"""

"""
로또 예시
"""
from __future__ import annotations # 선행참조(forward referencing). 이 방법 외에는 'ClassName'식으로 문자열 사용

class LottoNumber:
    _MIN_LOTTO_NUMBER:int = 1
    _MAX_LOTTO_NUMBER:int = 45
    _OUT_OF_RANGE:str = "로또번호는 1~45의 범위입니다."
    _NUMBERS:dict[int, LottoNumber] = {}

    def __init__(self, number: int):
        for i in range(self._MIN_LOTTO_NUMBER, self._MAX_LOTTO_NUMBER + 1):
            self._NUMBERS.update(i, LottoNumber(i))

        self.lotto_number = number

    def of(self, number: int):
        lotto_number:LottoNumber = self._NUMBERS.get(number)
        if lotto_number is None:
            raise ValueError(self._OUT_OF_RANGE)
        return lotto_number


