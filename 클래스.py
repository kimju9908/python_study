# 클래스
# 함수는 하나의 특정 작업을 수행하기 위해 독립적으로 설계된 프로그램 코드 입니다.
# 이 때 함수의 호출은 특정 작업만을 수행할 뿐 그 결과값을 계속 사용하기 위해서는 어딘가에 따로 저장 해야만 합니다.
# 클래스는 함수 뿐만 아니라 관련된 변수까지도 한꺼번에 묶어서 관리하도 재사용할 수 있게 해주는 것이 클래스** 입니다. (설계도와 유사한 개념)
# 파이썬에서 클래스는 `class`키워드를 사용하여 정의됩니다.
"""------------------------------------------------------------------------------------------------"""
# 객체
# 클래스를 이용해 객체를 생성할 수 있습니다.
# 객체는 속성과 행위로 구성된 대상을 의미합니다.
"""------------------------------------------------------------------------------------------------"""
# 객체지향 프로그램 특성
# 상속 :부모클래스의 특성을 자식 클래스에 물려주는 것을 의미하며 여러계층 구조로 상속도 가능하고
# 여러 부모로 부터 특성을 물려 받는 다중 상속도 가능 합니다.

# 캡슐화 :내부의 멤버의 값이 외부의 접근이 되지 않도록 값을 보호 합니다.
# 이 경우 게터와 세터라는 별도의 함수를 만들어 접근 해야 합니다.

# 다형성 :부모의 특성을 물려 받아 물려 받은 특성을 변경하거나 개선하는 등의 행위를 말 합니다.
# (오버로딩, 오버라이딩)

# 추상화 :객체화가 되지 않는 부모로 부터 특성을 물려 받는 경우를 말합니다.
# 실제화가 되지 않은 표준이나 규격등을 의미 합니다. (자바에서는 추상 클래스, 인터페이스)

# 파이썬에서 클래스를 사용하는 이유 - 코드 구조화, 코드 재사용, 상속과 다형성, 객체 지향 설계, 코드유지 보수 및 확장성
"""------------------------------------------------------------------------------------------------"""
# 생성자
# 생성자는 클래스가 객체로 만들어 질때 자동 호출 되며, 객체의 초기값을 지정 할 수 있습니다.
# 생성자 키워드 : __init__
# self는 자신의 객체를 가리키는 포인터 (객체 자신을 참조하는 매개변수)
# self는 현재 인스턴스 자신을 참조하는데 사용되며, 인스턴스 내의 속성에 접근하고 수정하는 데 사용됩니다.
# 클래스 이름은 파스칼표기법을 따르므로 첫자가 대문자이거나 전체를 대문자로 표기 합니다. (관례)

# class TV:
#     def __init__(self,name,isOn,channel,volume):
#         self.name = name # 인스턴스 변수를 생성하고 생성자의 매개변수 변수를 통해서 초기값 입력받음
#         self.isOn = isOn
#         self.channel = channel
#         self.volume = volume
#
#     def set_on(self,isOn):
#         self.isOn = isOn
#     def set_channel(self,cnl):
#         self.channel=cnl
#     def set_volume(self, vol):
#         self.volume = vol
#     def get_on(self):
#         return self.isOn
#     def get_channel(self):
#         return self.channel
#     def get_volume(self):
#         return self.volume
#     def view_tv(self):
#         power = ("OFF", "ON")
#         print(f"이름 : {self.name}")
#         print(f"전원 : {power[self.isOn]}")
#         print(f"채널 : {self.channel}")
#         print(f"볼륨 : {self.volume}")
#
# lg_tv = TV("LG", False,  10, 10)
# samsung_tv = TV("SAMSUNG", False, 20, 20)
# samsung_tv.view_tv()
# lg_tv.view_tv()
"""------------------------------------------------------------------------------------------------"""
# 메소드 오버라이딩
# 오버로딩은 파이썬에서 지원x
# 부모 클래스를 상속받아 동일안 매소드에 대해 재정의해 사용하는 것
# def over_sum(x,y,z):
#     return  x+y+z
# print(over_sum(1,2,3))
# print(over_sum(1.1,2.2,3.3))
# class ProtoTV:
#     def __init__(self, isOn, channel, volume):
#         self.isOn = isOn
#         self.channel = channel
#         self.volume = volume
#     def set_on(self, isOn):
#         self.isOn = isOn
#     def set_channel(self, cnl):
#         if 0 < cnl < 1000:
#             self.channel = cnl
#             print(f"채널을 {cnl}로 변경 하였습니다.")
#         else:
#             print(f"채널 설정 범위가 아닙니다.")
#     def set_volume(self, vol):
#         self.volume = vol
#     def get_on(self):
#         return self.isOn
#     def get_channel(self):
#         return self.channel
#     def get_volume(self):
#         return self.volume
# class TV(ProtoTV):
#     def set_channel(self, cnl):
#         if 0 < cnl < 2000:
#             self.channel = cnl
#             print(f"채널을 {cnl}로 변경 하였습니다.")
#         else:
#             print(f"채널 설정 범위가 아닙니다.")
#
# lg_tv = TV(False, 10, 10)
# samsung_tv = TV(False, 20, 20)
# samsung_tv.set_channel(1200)
# proto = ProtoTV(False, 10, 10)
# proto.set_channel(1000)
"""------------------------------------------------------------------------------------------------"""
#연산자 오버로딩
# 연산자의 기본 기능을 사용자가 정의 할 수 있게 한 것이다.
# 연산자 오버로딩은 내장 연산자들을 사용자 정의 클래스에 대해 다르게 동작하도록 재정의하는 것을 말합니다.
# 이를 통해 사용자 정의 객체에 대한 연산을 직관적이고 편리하게 처리할 수 있습니다.
# __add__(self, other): '+' 연산자에 대응합니다. 객체끼리 덧셈 연산을 정의합니다
# __sub__(self, other): '-' 연산자에 대응합니다. 객체끼리 뺄셈 연산을 정의합니다.
# __mul__(self, other): '*' 연산자에 대응합니다. 객체끼리 곱셈 연산을 정의합니다.
# __div__(self, other): '/' 연산자에 대응합니다. 객체끼리 나눗셈 연산을 정의합니다.
# __eq__(self, other): '==' 연산자에 대응합니다. 객체의 동등성 비교를 정의합니다.

# class Vector2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return Vector2D(self.x + other.x, self.y + other.y)
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
# v1 = Vector2D(1, 2)
# v2 = Vector2D(3, 4)
# v3 = v1 + v2  # '+' 연산자가 __add__ 메서드를 호출합니다.
# print(v3.x, v3.y)  # 출력: 4, 6
# print(v1 == v2)  # '==' 연산자가 __eq__ 메서드를 호출합니다.
"""------------------------------------------------------------------------------------------------"""
#인스턴스 메서드: 객체로 만들어 질 때 함께 만들어지는 메서드
"""------------------------------------------------------------------------------------------------"""
# 정적 메서드

# 정적 메소드는 클래스와 관련이 있어서 클래스 안에 두기는 하지만 클래스나 인스턴스(객체)와는 무관하게
# 독립적으로 동작하는 함수를 만들고 싶을 때 이용하는 함수 입니다.

# 함수를 정의할 때 인자로 self를 사용하지 않으며 정적 메서드 안에서는 인스턴스 메서드나 인스턴스 변수에 접근 할 수 없습니다.
# 용도 : 일반적인 함수처럼 동작, 클래스의 상태나 인스턴스의 상태와 관계없이 동작할 때 유용
# class Car :
#     isinstance_count = 0
#
#     # 초기화 함수
#     def __init__(self, size, model):
#         self.size = size   # 인스턴스 변수 생성 및 초기화
#         self.model = model
#         Car.isinstance_count = Car.isinstance_count + 1 # 클래스 변수 이용
#         print(f"자동차 객체 생성 수 : {Car.isinstance_count}")
#
#     def move(self, speed):
#         self.speed = speed
#         print(f"자동차 {self.size} & {self.model}가 시속 {self.speed}로 달립니다.")
#
#     @staticmethod
#     def check_type(code):
#         if(code <= 10): print("전기차 입니다.")
#         elif(code <= 20): print("가솔린차 입니다.")
#         elif(code <= 30): print("디젤차 입니다.")
#         else: print("분류 코드가 없습니다.")
#
# car1 = Car("소형", "모닝")
# car2 = Car("중형", "쏘나타")
#
# car1.move(90)
# Car.check_type(11)
# car2.move(70)
"""------------------------------------------------------------------------------------------------"""
#클래스 메서드
# 클래스 메서드는 클래스 변수를 사용하기 위한 함수 입니다.
# 클래스 메서드는 함수를 정의할 때 첫 번째 인자로 클래스를 넘겨받는 cls가 필요하며 이를 이용해 클래스 변수에 접근합니다.
# 용도 : 클래스 레벨에서 무언가를 해야 할 때 적합
# class Person:
#     count = 0  # 클래스 변수
#     def __init__(self):
#         Person.count += 1  # 인스턴스가 만들어질 때
#         # 클래스 속성 count에 1을 더함
#     @classmethod
#     def print_count(cls): #클래스 메서드
#         print('{0}명 생성되었습니다.'.format(cls.count))  # cls로 클래스 속성에 접근
#
# james = Person()
# maria = Person()
# Person.print_count()  # 2명 생성되었습니다.
"""------------------------------------------------------------------------------------------------"""
# 접근제한자와 게터/세터
# 파이썬에서는 자바의 private과 같은 엄격한 접근 제한자가 없습니다.
# 단지 네이밍 컨벤션과 관례를 사용하여 속성과 메서드의 가시성을 관리합니다.

# public: 기본값, 변수명 앞에 아무것도 붙이지 않음.
# protected: _변수명, 외부에서 접근 가능하지만 보호됨.
# private: __변수명, 클래스 외부에서 직접 접근 불가