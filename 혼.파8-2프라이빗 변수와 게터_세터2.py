#클래스 외부에서 직접  __radius 속성에 접근하는 방법
#게터(getter)/세터(setter):프라이빗 변수의 값을 추출/변경할 목적으로, 간접적으로 속성에 접근하도록 도와주는 함수
import math
#클래스를 선언
class Circle:
    def __init__(self,radius) :
        self.__radius=radius
    def get_circumference(self):
        return 2*math.pi * self.__radius
    def get_area(self):
        return math.pi*(self.__radius**2)
    #게터와 세터를 선언
    def get_radius(self):
        return self.__radius
    def set_radius(self,value):
        self.__radius=value
#원의 둘레와 넓이를 구합니다
circle=Circle(10)
print("#원의 둘레와 넓이를 구합니다")          #원의 둘레와 넓이를 구합니다
print("원의둘레:",circle.get_circumference()) #원의둘레: 62.83185307179586
print("원의넓이:",circle.get_area())          #원의넓이: 314.1592653589793
#간접적으로 __radius에 접근
print("#__radius 에 접근합니다.")              #__radius 에 접근합니다.
print(circle.get_radius())                    # 10
#원의 둘레와 넓이를 구합니다
circle.set_radius(2)
print("#반지름을 변경하고 원의 둘레와 넓이를 구합니다")
print("원의 둘레:",circle.get_circumference()) #원의 둘레: 12.566370614359172
print("원의 넓이:",circle.get_area())          #원의 넓이: 12.566370614359172

#게터 세터로 변수를 안전하게 사용하기
def set_radius(self,value):
    if value <=0:
        raise TypeError("길이는 양의 숫자여야 합니다")
    self.__radius=value
