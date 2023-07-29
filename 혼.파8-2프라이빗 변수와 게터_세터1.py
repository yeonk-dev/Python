#객체 지향 프로그래밍의 최종 목표: 객체를 효율적으로 만들고 사용하는 것
#원의 둘레와 넓이를 구하는 객체 지향 프로그램
import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def get_circumference(self):
        return 2*math.pi*self.radius
    def get_area(self):
        return math.pi*(self.radius**2)
circle=Circle(10)
print("원의 둘레:",circle.get_circumference())
print("원의 넓이:",circle.get_area())

circle=Circle(10)
circle.radius=-2 #음수인 경우 1.둘레는 음수로 나옴 2.길이는 양수로 나옴 3.길이를 음수로 넣는 것을 막을 방법 필요
print("원의 둘레:",circle.get_circumference()) #원의 둘레: -12.566370614359172
print("원의 넓이:",circle.get_area()) #원의 넓이: 12.566370614359172

#프라이빗 변수(변수를 마음대로 사용하고/클래스의 내부의 변수를 외부에서 사용하는 것을 막고 싶을 때) _ _<변수 이름>
import math
class Circle:
    def __init__(self,radius):
        self.__radius=radius
    def get_circumference(self):
        return 2*math.pi* self.__radius
    def get_area(self):
        return math.pi*(self.__radius**2)
circle=Circle(10)
print("#원의 둘레와 넓이를 구합니다")
print("원의 둘레:",circle.get_circumference()) #원의 둘레: 62.83185307179586
print("원의 넓이:",circle.get_area()) #원의 넓이: 314.1592653589793
print("#__radius에 접근합니다.")
print(circle.__radius) #AttributeError: 'Circle' object has no attribute '__radius'
#클래스 외부에서 __radius를 사용할 경우 오류 발생
