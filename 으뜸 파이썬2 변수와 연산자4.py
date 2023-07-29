#(3) 논리 연산자(logical operator) {True/False 부울(bool)}
print(10>20) #False
print(bool(9)) #True
print(bool(-1)) #True
print(bool(0)) #False
print(bool(None)) #False
print(bool('')) #False 빈 문자열
print(bool('hello')) #True 문자열
print(bool([])) #False 빈 리스트
print(bool([10,20])) #True 항목을 가진 리스트
x=True
y=False
print(x and y) #False
print(x or y) #True
print(not x) #False
#(2) 비트 연산자
# &(AND): 두 개의 피연산자의 해당 비트가 모두 1이면 1, 아니면 0
#  |(OR): 두 피연산자의 해당 비트 중 하나라도 1이면 1, 아니면 0
# ^(XOR): 두 개의 피 연산자의 해당 비트의 값이 같으면 0, 아니면 1
# ~(NOT): 0은 1로 만들고, 1은 0으로 만든다
# << :지정된 개수만큼 모든 비트를 왼쪽으로 이동시킴
# >> : 지정된 개수만큼 모든 비트를 오른쪽으로 이동시킴

#정수값의 2진수 출력
print(bin(9)) #0b1001
print(bin(10)) #0b1010
#9와 10의 비트 단위 AND 연산
print(9&10) #8
print(bin(8)) #0b1000
#9와 10의 비트 단위 or 연산
print(9|10) #11
print(bin(11)) #0b1011
#9와 10의 비트 단위 배타적 합 연산
print(9^10) #3
print(bin(3)) #0b11
#9의 비트 단위 부정연산자의 실행
print(~9) # -10
print(bin(-10)) #-0b1010
#비트 단위 이동 연산(시프트 연산<shift operter>)
#비트 단위 왼쪽 이동 연산 실습
print(4 <<1 ) #8
print(4<<2) #16
#비트 단위 오른쪽 이동 연산 실습
print(4>>1) #2
print(4>>2) #1
#LAB 2-9 :비트 연산 활용
a=1024
print(a >> 1) #512
print(a >> 2) #256
a=a>>1
print(a) #512
a=1
print(a << 1) #2
a=a<<1
print(a) #2
a= a<<1
print(a) #4
a=a<<1
print(a) #8
a=a<<1
print(a) #16

# 2.9 주석문
# (1) 한 줄 주석 처리하기
radius=4.0
print('원의 반지름', radius)
print('원의 면적', 3.14*radius*radius)
print('원의 둘레', 2.0*3.14*radius)
#주석을 넣은 후 코드
radius=5.0 #원의 반지름을 radius라는 변수로 정의함
print('원의 반지름', radius)         #원의 반지름과 면적,둘레를 각각 출력
print('원의 면적', 3.14*radius*radius)
print('원의 둘레', 2.0*3.14*radius)
#2-10  input() 문과 사용자 입력과 처리
name=input('이름을 입력하시오: ')
print('이름 :',name )
