#데코레이터를 사용한 게터와 세터
# @proerty / @<변수 이름>.setter
import math
class Circle:
    #...생략...
    #게터와 세터 선언
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self,value):
        if value <=0:
            raise TypeError("길이는 양의 숫자여야 합니다")
        self.__radius=value
print("#데코레이터를 사용한 Getter 와  Setter")
circle=Circle(10)
print("원래 원의 반지름:",circle.radius)
circle.radius=2
print("변경된 원의 반지름:",circle.radius)

print("#강제로 예외를 발생시킵니다")
circle.radius=-10