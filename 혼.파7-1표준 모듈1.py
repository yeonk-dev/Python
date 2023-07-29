#모듈(module)/표준 모듈-파이썬에 기본적으로 내장되어 있는 모듈 : 외부 모듈-다른 사람이 만들어서 공개한 모듈
#모듈 사용의 기본: math 모듈
import math
print(math.sin(1)) # 사인    :  0.8414709848078965
print(math.tan(1)) # 탄젠트  :  1.5574077246549023
print(math.cos(1)) #코사인   :  0.5403023058681398
print(math.floor(2.5)) #내림 :  2
print(math.ceil(2.5)) #올림  :  3
# log(x[,base]) 로그값 구하기
#반올림 함수(round): 정수 부분이 짝수 일때 5면 내리고, 홀수 일때 5면 올림
print(round(1.5)) #2
print(round(4.5)) #4
#from 구문 : from 모듈 이름 import 가져오고 싶은 변수 또는 함수 /여러 개의 변수 혹은 함수 입력 가능
from math import sin ,cos ,tan,floor,ceil
print(sin(1))
print(cos(2))
print(tan(1))
print(floor(2.5))
print(ceil(2.5))
#'math' 를 붙이지 않고 모든 기능을 가져오는 방법
from math import*

#as 구문 [import 모듈 as 사용하고 싶은 식별자]
#이름 충돌이 발생하거나 모듈의 이름이 너무 길어 짧게 줄여 사용하고 싶을 때
import math as m
print(m.sin(1))
print(m.cos(1))
print(m.tan(1))
print(m.floor(3.5))
print(m.ceil(3.5))


