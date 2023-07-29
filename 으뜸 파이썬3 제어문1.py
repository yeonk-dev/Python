#순차문
# num=100
# print('num =',num)
# num=num+100
# print(num) #200
# num=num+100
# print(num) #300

# #제어문
# # 3-2 : if 조건문을 이용한 출력기능(조건을 만족하는 경우)
# age=18
# if age<20:
#     print("청소년 할인") #청소년 할인
# # 3-3 : if 조건문을 이용한 출력기능(조건을 만족하지 않는 경우)
# age=24
# if age<20:
#     print("청소년 할인") #출력 없음
# #lab 3-1: if 문의 사용법
# num_a=300
# num_b=300
# if num_a==num_b:
#     print('두 값이 일치합니다') 
# #조건문과 블록
# # age=18
# # if age<20:
# # print('청소년 할인') - IndentationError: expected an indented block
# #if 문 다음엔 들여쓰기 블록(indented block)
# #들여쓰기 코드1(조건 만족)
# age=18
# if age<20:
#     print('청소년 할인')   #청소년 할인
# print('입장을 환영합니다') #입장을 환영합니다
# #들여쓰기 코드2(조건 불만족)
# age=24
# if age<20:
#     print('청소년 할인')   
# print('입장을 환영합니다') #입장을 환영합니다
# #들여쓰기 코드3(조건 만족)
# age=18
# if age<20:
#     print('나이',age)  #나이 18
#     print('청소년 환영') #청소년 환영
#     print('청소년 할인') #청소년 할인
# #들여쓰기 코드4(조건 불만족)
# age=24
# if age<20:
#     print('나이',age)  
#     print('청소년 환영') 
#     print('청소년 할인') #아무것도 출력 X /들여쓰기 블록 전체가 수행되지 않음
# #들여쓰기 코드5(들여쓰기 크기가 일정하지 않음)
# # age=18
# # if age<20:
# #     print('나이',age)  
# #   print('청소년 환영')  IndentationError: unindent does not match any outer indentation level

# #대화형 모드의 블록
# num=300
# if num > 200:
#     print('num은 200보다 큽니다')
# ...
# #코드3-6 : 3의 배수를 판단하기 위한 모듈로 연산과 조건문
# number= int(input('정수를 입력하세요 : '))
# if number % 3 ==0:
#     print(number, '은 3의 배수입니다')
# #코드3-6 : 3과 5의  배수를 판단하기 위한 모듈로 연산과 and 조건문
# number= int(input('정수를 입력하세요 : '))
# if number % 3 ==0 and number%5==0:
#     print(number, '은 3의 배수이면서 5의 배수입니다')

#lab 3-2: 변수와 if 조건식 사용하기
# n=int(input(''))
# print('정수를 입력하세요: ',n)
# print('n =',n)
# if n%2==0:
#     print(n,'은 짝수입니다')

# x=int(input())
# print('정수를 입력하세요',x)
# print('x =',x)
# if x>=0:
#     print(x,'는 자연수 입니다')

#3.3 ) if-else 조건문

#코드3-8: if 문을 이용한 '오전' 혹은 '오후'의 출력기능
# hour=10
# if hour<12:
#     print('오전입니다')
# if hour>=12:
#     print('오후입니다')
# #코드3-9: if-else 문을 이용한 '오전' 혹은 '오후'의 출력기능
# hour=10
# if hour<12:
#     print('오전입니다')
# if hour>=12:
#     print('오후입니다')
#코드 3-10: if-else 문을 이용한 '음수' 혹은 '음수 아님'의 출력기능
num = -10
if num<0:
    print(num, '은 음수입니다')
else:
    print(num, '은 음수가 아닙니다')
#코드 3-11: if-else 문을 이용한 '짝수' 혹은 '홀수'의 출력기능
num=10
if num%2==0:
    print(num, '은 짝수입니다')
else:
    print(num, '은 홀수입니다')
#코드3-12: 외부 if-else 문과 내부 if-else 문의 사용
num=101
if num<0:
    print(num, '은 음수입니다')
else:
    print(num, '은 음수가 아닙니다.')
    if num%2==0:
        print(num, '은 짝수입니다')
    else:
        print(num, '은 홀수입니다')
