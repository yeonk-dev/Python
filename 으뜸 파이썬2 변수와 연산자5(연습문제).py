#연습문제
#2-1
# print(100,'+', 200,'=', 100+200)
# print(200,'+', 300,'+', 400,'=', 200+300+400) #200 + 300 + 400 = 900
# #2-2
# width=30
# height=60
# print(width) #30
# print(height) #60
# #2-3
# width=30
# height=60
# area=width*height
# print("사각형의 면적 :", area) #사각형의 면적 : 1800
# #2-4
# width=40
# height=20
# area=int((width*height)/2)
# print("사각형의 면적 :", area) #삼각형의 면적 : 400
# #2-5
# 밑변=int(input("정사각형의 밑변을 입력하시오 : "))
# print('정사각형의 면적 :', 밑변**2)
# #2-6 
# # j=0
# # for i in range(1,10+1,1):
# #     j+=i
# # print('1에서 10까지의 합 :', j)
# print("1에서 10까지의 합 : ",1+2+3+4+5+6+7+8+9+10)
# #2-7
# j=1
# for i in range(1,10+1,1):
#    j*=i
# print("10! =",j)

# print("10! =",1*2*3*4*5*6*7*8*9*10) #10! = 3628800

#2-8
# n=2
# print("a", "n", "a**n")
# for a in range(2,6+1,1):
#     print(int(a), int(n), int(a**n))

# n=2
# print("a", "n", "a**n")
# print(2, n, 2**n)
# print(3, n, 3**n)
# print(4, n, 4**n)
# print(5, n, 5**n)
# print(6, n, 6**n)

# #2-9(못푼 문제)
# # print('섭씨\t',end='')
# # print('화씨')
# # for c in range(0,50+1,10):
# #     f=(9/5)*c+32
# #     print(f'{c}\t{f}')
# print("섭씨",   "화씨")
# print(0,   (9/5)*0+32)
# print(10,   (9/5)*10+32)
# print(20,   (9/5)*20+32)
# print(30,   (9/5)*30+32)
# print(40,   (9/5)*40+32)
# print(50,   (9/5)*50+32)


# print('섭씨','화씨')
# for c in range(0,50+1,10):
#     f=(9/5)*c+32
#     print(f'{c}\t{f}')

# #2-10
# celsius=int(input('섭씨온도를 입력하세요 :'))
# fahrenheit=float((9/5)*celsius+32)
# # print(f'섭씨 {celsius} 도는 화씨 {fahrenheit} 도 입니다')
# print('섭씨',celsius,'도는 화씨',fahrenheit,'도 입니다')
# # # #2-11
# fahrenheit=int(input('화씨온도를 입력하세요 :' ))
# celsius=float((fahrenheit-32)/(9/5))
# print(f'화씨 {fahrenheit} 도는 화씨 {celsius} 도 입니다')

# #2-12
# PI=3.141592
# radius=11
# print("원의 반지름=",radius, "원의 둘레 =", 2*PI*radius,"원의 면적 = ", PI*radius**2)      
# #2-13
# PI=3.141592
# radius=11
# print("원의 반지름을 입력하세요: ",radius)
# print("원의 둘레 = ",2*PI*radius,"원의 면적 = ",PI*radius**2)
# #2-14
# for c in range(2,10+1,1):
#     print(f'{c}의 제곱근 = {c**(1/2)}')
#2-15
# ver = int(input("밑변 : "))
# hor = int(input("높이 : "))
# sid = (ver*ver) + (hor*hor)
# print('빗변:',sid**(1/2))

# #2-16
# import math as m #cos sin을 계산하기 위한 모듈

# def rotate(x,y,a): # rotate라는 함수를 선언, x=복소수에서 실수부,  y=허수부 a=각도(60,90,360...)
#     before=complex(x,y) #복소수를 선언 방법 2가지 1) 2+3j 수학에서는 i로표시하지만 파이썬 에서는 j또는J로 표시 
#     #두번째 표기방법은 complex(실수부,허수부)
#     print(before)
#     r=m.radians(a)#degree를 radians 로 변환
#     after=before*complex(m.cos(r),m.sin(r)) #문제에서 나온대로 연산
#     print(after)
#     return after #결과를 반환
# print(rotate(1,2,90))

#예시
# a=8+2j
# b=4+3j
# print(a*b) #(1+2j)*(0+1j)=-2+1j

# c=1+2j
# d=2+1j
# x=d/c
# print(x)
#(1)
# before=1+2j
# print('회전하기 전:',before)
# after1=(1+2j)*(0+1j)
# print('90도 회전한 후',after1)

# c1=1+2j
# c2=(0+1j)*c1
# print(c2)

# #(2)
# before1=1+2j
# print('회전하기 전: ',before1)
# after1=(1+2j)*(3**(1/2)/2 + -1/2j)
# print('30도 회전한 후',after1)

# c1=1+2j
# c2=(3**(1/2)/2 + -1/2j)*c1
# print(c2)

#2-17 비트 이동 연산자 
# print(2<<0,2<<1,2<<2,2<<3,2<<4,2<<5,2<<6,2<<7,2<<8,2<<9)
n=2
for i in range(0,10):
    print(f'{2<<i}',end=' ')


#2-18
# n=int(input("정수를 입력하세요 : "))
# if n%2==0:
#     print("이 수가 짝수인가요? True")
# else:
#     print("이 수가 짝수인가요? False")
#2-19
a=int(input("정수를 입력하세요 : "))
if 0<= a <= 100 and a%2==0:
    print('입력된 정수는 0에서 100의 범위 안에 있는 짝수 인가요? True')
else:
    print('입력된 정수는 0에서 100의 범위 안에 있는 짝수 인가요? False')

#2-20
# print(bin(5)) #0b101
# print(bin(6)) #0b110
# print(bin(5&6)) #0b100
# print(bin(5|6)) #0b111
# print(bin(5^6)) #0b11
#2-21
# a=int(input())
# print("정수를 입력하시오 :",a)
# print(f'{a}의 2진수 값 :',bin(a))
# print(f'{a}의 2진수 값에 대한 비트단위 부정값 :', bin(-(~a)))
# #2-22
# a=int(input())
# b=int(input())
# print("정수 a를 입력하시오 :", a)
# print("정수 b를 입력하시오 :", b)
# print("a / b의 몫 :", a//b)
# print("a / b의 나머지 : ", a%b)
#2-23
# n=int(input())
# print("세 자리 정수를 입력하세오 : ", n)
# print("백의 자리 : ",n//100)
# print("십의 자리 : ", n%100//10)
# print("일의 자리 : ", n%10)

#2-24
# n=int(input("세 자리 정수를 입력하세오 : "))
# print(n%10)
# print(n%100//10)
# print( n//100)

# n=int(input("세 자리 정수를 입력하세오 : "))
# print(n%10,n%100//10,n//100)

