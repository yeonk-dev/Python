#2-3 변수의 생성과 식별자
width=10
height=5
rectangle_area= width*height
print('사각형의 면적:',rectangle_area) #사각형의 면적: 50
name='장연경'
print('나의 이름은=',name) #나의 이름은= 장연경
age=27
print('나의 나이는=',age)
height=179
print('나의 키는=',height)
sum=10+20
print('10+20=',sum) #10+20= 30
mult= 10*20
print('10*20=',mult)
#lab 2-5 :다양한 식별자를 활용한 변수 활용
#global=300
#print(global) #SyntaxError: invalid syntax (파이썬 키워드는 사용 용도가 고정되어 변수로 사용 불가능)
# width=20
# height=40
# area=(width*Height)  ==NameError: name 'Height' is not defined
# print('사각형의 면적',area)
width=20
height=40
area=(width*height)  
print('사각형의 면적:',area)

iixxjjkk=20
print('나의 나이는',iixxjjkk,'세 입니다') #변수 이름이 명확하지 않음
v1=1
v2=2
thisissaverylongvariablename= v1+v2
print(thisissaverylongvariablename) ##변수 이름이 명확하지 않음/ 이름이 너무 길음
radius=20
depth=10
final_length=0.5*radius*depth
print('삼각형의 면적은',final_length)
# 1st_year=30
# 2st_year=30
# all_year+=1st_year+2st_year
# print(all_year+)  SyntaxError: invalid syntax (숫자 1로하는 식별자는 사용 불가능)

#코드 2-5변수에 값을 지정하고 출력하기
name='장연경'
age=20
print('안녕! 나는',name,'이야, 나는 나이가', age,'살이야') #안녕! 나는 장연경 이야, 나는 나이가 20 살이야
#lab 2-6 변수 값의 재지정
width=20
height=40
width=30
area=width*height
print(area) #1200

#2-4 변수와 연산자
print(11/2) #실수 나눗셈
print(11//2) #정수 나눗셈 연산 - 몫을 구함
print(4**0.5) #거듭제곱- 4의 제곱근을 구함
print(10%5) #10을 5로 나눈 나머지를 구함

print(2**0.5)

#코드 2-7(p.68): 문자열과 정수의 덧셈연산
# my_age=20
# my_height='177' -TypeError: can only concatenate str (not "int") to str
# my_age=my_age+1
# my_height=my_height+1
# print(my_age,my_height)
#LAB 2-7 : 파이썬 연산자의 사용
#3 제곱근 구하기
print(2**0.5) #1.4142135623730951
print(3**0.5) #1.7320508075688772

my_age=20
my_height=177.5
my_age=my_age+1
my_height=my_height+1
print(my_age,my_height) #21 178.5

#(1) 거듭제곱 연산의 적용
print(4**0.2) #1.3195079107728942
print(0.2**4) #0.0016000000000000003

#2-5 자료형의 의미와 자료형 확인
num=85
print(type(num)) #<class 'int'>
pi=3.14159
print(type(pi)) #<class 'float'>
message= 'good morning'
print(type(message)) #<class 'str'>
#동적 형결정의 이해
foo=100
print(type(foo)) #<class 'int'>
foo="str"
print(type(foo)) #<class 'str'>
#다양한 자료형의 이해
i=[123,456,789,34]
print(type(i)) #<class 'list'>
f={'apple':3000,'banana':4000}
print(type(f)) #<class 'dict'>
t=('홍길동',0.45,6)
print(type(t)) #<class 'tuple'>
#str() 함수 실습
print(str(100))
x=['a','b','c']
print(str(x))
#2-6 문자열 자료형
txt1='강아지 이름은"햇님"이야'
print(txt1) #강아지 이름은"햇님"이야
txt2='강아지 이름은 "단비"여'
print(txt2) #강아지 이름은 "단비"여
# txt3="친구가 "비가"좋아 라고 말했다"
# print(txt3) #SyntaxError: invalid syntax
txt4="친구가 \"햇님이 좋아\"라고 말했다"
print(txt4) #친구가 "햇님이 좋아"라고 말했다 ==둘 이상이 연속적으로 나타나거나 중간에 공백문자나 줄바꿈 문자가 있더라도 이를 하나의 연속적인 문자열로 간주
txt5='Hello ''Python'
print(txt5) #Hello Python
txt6='apple\nfresh\norange'
print(txt6) #역슬래시 "\" == 이스케이프(escape) 문자
txt7='''Let's go'''
print(txt7) #Let's go
txt8='''큰따옴표(")와 작은 따옴표(')를 모두 포함한 문장'''
print(txt8) #큰따옴표(")와 작은 따옴표(')를 모두 포함한 문장
long_str="""사과는 맛있어 
맛있는 건 바나나"""
print(long_str)  #줄 바꿔서 프린트
