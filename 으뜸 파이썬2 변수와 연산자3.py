#2.7 수치 자료형
#정수형(integer):소수점이 없는 숫자 / 실수형(float):소수점이 있는 숫자
print(1+2)
print(5.0==5.00) #True
#자료형의 표현 능력과 수치오류
#(1)부동소수점 수의 수치오류
print(0.1+0.1==0.2) #True
print(0.1+0.1+0.1==0.3) #False
print(0.1+0.1+0.1) #0.300000000000000034
print(0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1)#0.7999999999999999
print(0.1*19.0) #1.9000000000000001
#정수 표현의 한계 
print(10**100) #10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
print(14.2-(5.3*2.0)) #3.5999999999999996
#(2)복소수 자료형
#c=2+3i ==SyntaxError: invlalid syntax & 허수부에 "i"를 사용하면 오류가 발생
c1=2+3j
print(c1.real) #2.0- c1의 실수부 출력
print(c1.imag) #3.0- c1의 허수부 출력
c2= 5+6j
c3= 6+2j
print(c2+c3) #(11+8j)
#켤레 복소수 표현과 크기 구하기
c1=2+3j
c2=c1.conjugate()
print(c2) #(2-3j)
print(abs(c1)) #3.605551275463989
c3= c1*c2
print(c3) #(13+0j)
print(abs(c1)*abs(c1)) #12.99999999999999
#lab 2-8 : 복소수의 연산
a=8+2j 
b=4+3j
print(a+b) #(12+5j)
print(a-b) #(4-1j)
print(a*b) #(26+32j)
print(a/b) #(1.52-0.64j)
#2-8 여러 가지 연산자
#(1) 할당(assign) 연산자 +다중 할당(multiple assignment)
#다중 할당과 동시 할당
num1=num2=num3=200
print(num1,num2,num3) #200 200 200
num4,num5= 300,400
print(num4,num5) #300 400
#할당 연산 실습
result1=10*20
print(result1) #200
result2=(2*3)-(4**2) / 2
print(result2) #-2.0
#print(300=300) #SyntaxError: can't assign to literal/SyntaxError: keyword can't be an expression
# str='world'
# 'hello'=str  #SyntaxError: can't assign to literal 리터럴에는 변수 할당X
num=200
num=num+100
print(num) #300
#할당 연산자와 사칙연산
num=200
num=num+100
print(num) #300
num=num-100
print(num) #200
num=num*20
print(num) #4000
num=num/2
print(num) #2000.0
#복합 할당 연산과 그 수행 결과
num=200
num+=100
print(num) #300
num-=100
print(num) #200
num*=20
print(num) #4000
num/=2
print(num) #2000.0
#(2) 비교 연산자
# "==" 같다 "!=" 다르다 ">" 왼쪽 보다 오른쪽이 크다 "<"왼쪽이 오른쪽보다 작다 
#">=" 왼쪽이 오른쪽보다 크거나 같다 "<=" 왼쪽이 오른쪽보다 작거나 같다
a,b=100,200
print(a==b) #False
print(a != b) #True
print(a>b) #False
print(a<b) #True
print(a>=b) #False
#(a > = b) SyntaxError: invalid syntax
#print(a =>b)  SyntaxError: invalid syntax

#(3) 논리 연산자(logical operator) {True/False 부울(bool)}
print(10>20)