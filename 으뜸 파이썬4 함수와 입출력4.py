#4.7 재귀함수
#코드 4-29: 재귀함수를 이용하여 정의한 팩토리얼
# def factorial(n): # n!의 재귀적 구현
#     if n<=1:             #종료조건이 반드시 필요하다
#         return 1
#     else:
#         return n*factorial(n-1) #n * (n-1)! 정의에 따른 구현
# n=5
# print(f'{n}!={factorial(n)}') #5!=120
# #코드 4-30: 재귀함수를 이용하여 정의한 피보나치 수열
# def fibonacci(n):
#     if n<=1:     #피보나치 함수의 종료조건
#         return n
#     else:
#         return(fibonacci(n-1)+fibonacci(n-2))
# nterms=int(input('몇 개의 피보나치수를 원하세요? '))
# if nterms<=0: #음수일 경우 피보나치 수를 구할 수 없음
#     print('오류 : 양수를 입력하세요')
# else:
#     print('Fibonacci 수열:',end='')
#     for i in range(nterms):
#         print(fibonacci(i), end=' ')

#4.8 입력함수와 출력함수
#코드 4-31: input() 입력함수를 이용한 name의 입력 방법
# print('Enter your name : ')
# name=input()
# print('hello',name,'!')   
# #코드 4-32: 문자열을 이용한 input 입력함수의 사용법
# name=input('Enter your name :')
# print('hello',name,'!')
#4.8.1 input() 함수와 int() 함수
#실습 :  정수형과 문자열형의 덧셈, 서로 다른 자료형의 덧셈
# print('100'+1) #TypeError: can only concatenate str (not "int") to str
#실습 :  int() 함수와 float(), str() 함수를 이용한 문자열의 반환
# print(int(100)+1) #101
# print(float(100+1)) #101.0
# #실습 :  대화형 모드를 통한 input()과 int() 함수
# num1=int(input('숫자 입력:'))
# num2=int(input('숫자 입력:'))
# num3=num1+num2
# print('두 수 합 :',num3)
#실습 :  input() 함수와 공백 구분자를 사용한 split() 메소드
# s1,s2=input('문자열 2개를 입력하세요:').split()
# print(s1, s2)
#실습 :  공백 구분자를 사용한 input() 함수 실습
# num1,num2,num3=input('세 정수 입력:').split()
# num1,num2,num3=int(num1),int(num2),int(num3)
# print(num1,num2,num3)
#실습 :  쉼표 구분자를 이용한 input() 함수 실습
# num1,num2,num3=input('세 정수 입력:').split(',')
# num1,num2,num3=int(num1),int(num2),int(num3)
# print(num1,num2,num3)

#4.8.2 형식출력을 위한 format() 메소드
#실습: 여러가지 문자열 메소드
# print('hello'.upper()) #HELLO
# print('got it yeay'.split()) #['got', 'it', 'yeay']
# print('rt,ty,uy'.split(',')) #['rt', 'ty', 'uy']
# print('rt|ry|ui'.split('|')) #['rt', 'ry', 'ui']
# s='aaa'
# s1='aaaaaa'
# print(s.count('a')) #3
# print(s1.count('a')) #6
# #실습: format()메소드와 플레이스 홀더
# print('{} python!'.format('hello')) #hello python!
# print('{} python!'.format('hi')) #hi python!
# #실습 : format()메소드와 플레이스 홀더의 인덱스
# print('i like {} and {}'.format('book','hat')) #i like book and hat
# #실습 : format()메소드와 플레이스 홀더의 인덱스2
# print('i like {1} and {0}'.format('book','hat')) #i like hat and book
# #실습: format() 메소드와 플레이스 홀더의 인덱스 사용법
# print('{0}, {0}, {0}! python!'.format('hello')) #hello, hello, hello! python!
# print('{0}, {0}, {0}! python!'.format('hello','hi'))  #hello, hello, hello! python!
# print('{0} {1}, {0} {1}, {0} {1}!'.format('hello','python')) #hello python, hello python, hello python!
# #실습: 플레이스 홀더 내의 객체 출력
# greet='hello'
# print('{} world'.format(greet)) #hello world

#코드 4-33 : 플레이스홀더와 format() 메소드의 사용
# name='jang yeonkyeoung'
# print('my name is {}'.format(name))
#코드 4-34 : 플레이스홀더와 format() 메소드의 사용2
# name=input('이름:')
# age=int(input('나이:'))
# job=input('직업:')
# print(f'당신의 이름은 {name}, 나이는 {age} 살, 직업은 {job}입니다.')

#lab 4-11 : format 메소드의 활용
#name=input('이름:')
#age=int(input('나이:'))
#job=input('직업:')
#city=input('사는 곳을 입력해 주세요:')
#print(f'당신의 이름은 {name}, 나이는 {age} 살, 직업은 {job},사는 곳은 {city}입니다')
#2
#print('당신의 이름은',name,'나이는',age,'살 직업은 ',job,'사는 곳은',city,'입니다')

#4.9 고급 format()메소드
#실습: 정수 표현을 위한 기본 포멧팅
#for i in range(2,15,2):
#    print('{0} {1} {2}'.format(i,i*i,i*i*i))
#실습: 출력 간의 크기 지정을 통한 정수 포메팅
#for i in range(2,15,2):
#    print('{0:3d} {1:4d} {2:5d}'.format(i,i*i,i*i*i))
#실습: 소수점 아래 자리수를 조절하는 실수 포메팅
#print('소수점 두자리로 표현한 원주율 = {0:10.2f}'.format(3.1415926)) #소수점 두자리로 표현한 원주율 =       3.14
#print('소수점 세자리로 표현한 원주율 = {0:10.3f}'.format(3.1415926)) #소수점 세자리로 표현한 원주율 =      3.142
#실습: 실수 표현을 위한 포메팅에서 소수점
#print('1/3은 {:.3f}'.format(1/3)) #1/3은 0.333
#실습 : 1000단위 쉼표 출력 방법
#print('{:,}'.format(12345567)) #12,345,567
# 실습 : 플레이스 홀더 내에 키-값 형식으로 인자를 전달하는 방법
# print('위도 {0}, 경도 {1}'.format('35.17N','129.07E')) #위도 35.17N, 경도 129.07E
# print('위도 {lat}, 경도 {long}'.format(lat='35.17N',long='129.07E'))

#4.10 문자열의 다양한 메소드
#실습 : 문자열의 다양한 메소드
print('abc'.upper()) #ABC #upper()=대문자로 만들어줌
print('ABC'.lower()) #abc #lower()=소문자로 만들어줌
print('hooby'.count('h')) #1 count()=문자가 나타나는 횟수
print('hobby'.count('b')) #2
print('hobby'.find('h')) #0 find()= 문자의 위치 반환
#실습 : 문자열의 메소드 실습
print(','.join('ABCD')) #A,B,C,D
print('       hello'.rstrip()) #rstrip()=오른쪽 공백 지우기
print('       hello'.lstrip()) #lstrip()=왼쪽 공백 지우기
print('    hello    '.strip()) #strip()=공백 지우기
s='long live the king!'
print(s.replace('king','queen')) #long live the queen! replace()=문자열 교환
print(s.title()) #Long Live The King! #title()=타이틀 문자열로 반환
print(s.capitalize()) #Long live the king! # capitalize()=첫 문자만 대문자로 변환
s2='X:Y:Z'
print(s2.split(':')) #['X', 'Y', 'Z'] #split(':'):를 구분자로 하여 s2 문자를 리스트로 분리함
print('hi ' +'python!') #hi python! # '+' 연산자를 이용하여 문자를 연결함
#lab 4-12:문자열의 여러 메소드 활용
print('_'.join('ABCD')) #A_B_C_D
s='My favorite thing is monsters'
print(s.replace('monsters','cartoons')) #My favorite thing is cartoons

#4.11 내장함수
#실습 : 대화형 모드를 통한 여러가지 내장함수 실습
print(abs(-100)) #100 #abs()=절댓값을 반환하는 함수
print(min(100,200,300,50)) #50 #min()=최소값을 반환하는 함수
print(max(100,200,300,50)) #300 #max()=최대값을 반환하는 함수
str1='FOO' #foo 혹은 FOO 형식으로 문자열 객체를 반환함
print(len(str1)) #3 #len()=문자열의 길이를 반환
print(eval("100+200+300")) #600 #eval()=문자열을 수치값과 연산자로 반환하여 평가
print(sorted("EABFD")) #['A', 'B', 'D', 'E', 'F'] # sorted()= 문자열을 정렬
list=[200,100,50,70]
print(sorted(list)) #[50, 70, 100, 200]
print(sorted(list, reverse=True)) #[200, 100, 70, 50] 거꾸로 출력
#실습: 대화형 모드를 통한 id() 함수 실습
a_str="hello py!"   #id()=객체의 식별값을 정수형으로 반환
print(id(a_str)) #2081600467952
n=300
print(id(n)) #2401956725296
#실습: 여러가지 자료형에 대한 type() 함수의 적용
print(type(123)) #<class 'int'>
print(type('hello')) #<class 'str'>
print(type(123.4)) #<class 'float'>
print(type([100,200,300])) #<class 'list'>
print(type(("딸기",100,103,True))) #<class 'tuple'>
#실습: 수식을 가진 문자열과 eval() 함수,chr(), ord() 함수
print(eval('10+20')) #30 #10+20 의 문장을 파이썬 번역기가 수행함
print(eval('(5*20) /2')) #50.0
print(chr(65)) #A #유니코드 값 65는 알파벳 A이며, chr() 함수는 이를 반환
print(ord('A')) #65 # 알파벳 'A'의 유니코드 값 65를 반환함
