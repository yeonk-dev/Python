#연습문제 1.1
import os
print("현재 운영체제:",os.name)
#파이썬 인트르리터 버전:Python 3.10.8

#연습문제 1.2
#java : 객체 지향 언어 ,인터프리터 언어,독립적인 플랫폼
#C : 구조화된 언어, 이식성, 확장성, 표현법
#C++ : 객체의 캡슐화(자료 은닉), 상속성(재사용성), 다형성
#Swift : 스트롱 타입 시스템, 불변성 , 프로퍼티
#C# : 객체 지향 언어, .NET Frame Work , 안전한 형
#JavaScript : HTML/CSS와 완전히 통합할 수 있음,간단한 일은 간단하게 처리할 수 있게 해 줌,모든 주요 브라우저에서 지원하고 기본 언어로 사용됨

#연습문제1.3
print(100)
print(100+200)
print('100+200')
print(100,200)
print('100','200')
print('100''200')
print('Hello Python!')
print('Hello','Python', '!')
print('Hello'+'Python'+'!')
print('Hello''Python''!')
print("**********")
print('*'*10)
#연습문제1.4
print('Hello Python!')
#print("Hello Python!')-SyntaxError: EOL while scanning string literal
#print(Hello Python!)-SyntaxError: invalid syntax
#print(100+'200')-TypeError: unsupported operand type(s) for +: 'int' and 'str'
#연습문제1.5
print("Welcome to Python!!")
print("Welcome to Python!!")
print("Welcome to Python!!")
print("Welcome to Python!!")
print("Welcome to Python!!")
#연습문제1.6
print('*'*36)
print("안녕하세요~")
print("저는 장연경입니다")
print("경기과학기술대학교 컴모융 1학년 입니다")
print('*'*36)
#연습문제1.7
star=8
i=3
for k in range(1, star, 2):
    j=(star-k)/2
    print(" "*int(j)  ,"*"*k)
#연습문제 1.8
star=8
i=3
for k in reversed(range(1, star, 2)):
    j=(star-k)/2
    print(" "*int(j)  ,"*"*k)

a=int(input("줄개수"))
start=2*a-1
for i in range(a):
    print(' '*i+"*"*(start-2*i))
#1.9
print(400-200)
print(45*89)
print(32/8)
print(9*3)
print(9**3)
print(9/3)
print(9//3)
print(9%3)
#1.10
#(1)
x=1
sum=0

while x < 10:
    sum = sum + x
    x = x+1
print(sum)
#(2)
pi=3.14
r=5
print(2*pi*r)
#(3)
j=25
print(j*4)
#(4)
print(j**2)
#(5)
밑변=30
높이=10
print((밑변+높이)*2)
#(6)
밑변=30
높이=10
print(밑변*높이)

#1.11
속력=80
시간=1.5
print(속력*시간,"km")
#1.12
거리=190
시간=2
print(거리/시간,"km")
#1.13
평균거리=149597870
초당이동거리=299792
print(평균거리/초당이동거리,"초")
#1.14
def factorial(n):
    output=1    
    for i in range(1,n+1):
        output*=i
    return output
print("1!=",factorial(3)) #1!=1
print("5!=",factorial(5)) #5!=120
print("12!=",factorial(12))
print("20!=",factorial(20))
#1.15
# a,b=map(int,input().split())
# print(f"{a}와 {b}의 평균값:{(a+b)/2}")

print("100과 200의 평균값:",int((100+200)/2))
#1.16
# a,b=map(int,input().split())
# print(f"{a}+{b}={a+b}")
# print(f"{a}-{b}={a-b}")
# print(f"{a}*{b}={a*b}")
# print(f"{a}/{b}={a/b}")
print("50 + 30 =",50+30)
print("50 - 30 =",50-30)
print("50 * 30 =",50*30)
print("50 / 30 =",50/30)
#1.17
print("4 + 5 =",4+5)
print("10 - 20 =",10-20)
print("6000 * 3000 =",50*30)
print("60000000 / 30000000 =",60000000/30000000)
