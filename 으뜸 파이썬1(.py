#1-1 : Hello World 출력하기
print("Hello World")
#대화창에서 문자열과 숫자 출력하기
print("Hello World") #Hello World
print('Hello','World') #Hello World
print('Hello'+'World') #HelloWorld
print(100) #100
print(2+4) #6
#대화창에서 간단한 숫자 출력
print('100+200')
print(100,200)
print('100','200')
print('100''200')
print('Hello','Python', '!')
print('Hello'+'Python'+'!')
print('Hello''Python''!')
print('**********')
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
# star=8
# for k in range(1, star, 2):
#     j=(star-k)/2
#     print(" "*int(j)  ,"*"*k)

print(     "*")
print(    "***")
print(   "*****")
print(  "*******")
   
#연습문제 1.8
# star=8
# for k in reversed(range(1, star, 2)):
#     j=(star-k)/2
#     print(" "*int(j)  ,"*"*k)

# a=int(input("줄개수"))
# start=2*a-1
# for i in range(a):
#     print(' '*i+"*"*(start-2*i))

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
#(1) 1에서 10까지 자연수의 합
x=1
sum=0

while x < 10:
    sum = sum + x
    x = x+1
print(sum)
print(1+2+3+4+5+6+7+8+9+10)

print('1에서 10까지 자연수의 합:',1+2+3+4+5+6+7+8+9+10)
#(2) #반지름의 길이가 5인 원의 둘레
pi=3.14
r=5
print(2*pi*r)
#(3) 한 변의 길이가 25인 정사각형의 둘레
j=25
print(j*4)
#(4) 한 변의 길이가 25인 정사각형의 면적
print(j**2)
#(5) 높이가 10이고 밑변이 30인 직사각형의 둘레
밑변=30
높이=10
print((밑변+높이)*2)
#(6) 높이가 10이고 밑변이 30인 직사각형의 면적
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
    output=1    #어떤 값에 곱해도 변화가 없는 1을 초기값으로 선언
    for i in range(1,n+1):
        output*=i
    return output
print("1!=",factorial(3)) #1!=1
print("5!=",factorial(5)) #5!=120
print(factorial(12))
print(factorial(20))
#1.15
a,b=input().split()
a=int(a)
b=int(b)
print(f"{a}와 {b}의 평균값:{(a+b)/2}")
#1.16
a,b=map(int,input().split())
print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a/b}")