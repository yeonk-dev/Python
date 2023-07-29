#lab 3-3: if 조건문의 응용
#1
# num=int(input( ))
# print('게임정수를 입력하시오 :',num)
# print('game_score =',num)
# if num>=800:
#     print("입문자입니다")
# else:
#     print("고수입니다")
# #2
# a,b=map(int,input().split())
# print('한 정수를 입력하시오 :',a)
# print('다른 정수를 입력하시오 :', b)
# if a==b:
#     print('두 값이 일치합니다')
# else:
#     print('두 값이 일치하지 않습니다')
#3
age=int(input('당신은 성인인가요(성인이면 1, 미성년이면 0):'))
if age==1:
    su=int(input('결혼을 하셨나요(기혼이면 1, 미혼이면 0):'))
    if su==1:
        print('당신은 결혼한 성인입니다')
    else:
        print('당신은 결혼하지 않은 성인입니다')

#복합 조건식

#조건식 실습
# print(0<10) #True
# print(4>10) #False
# print(3<=10) #True
# print(15 >= 10 ) #True
# print(1 ==2) #False
# print(True or False) #True
# print(True and False) #False
# #코드 3-13 : and와 or 조건문의 사용법
# a=10
# b=13
# if (a%2==0) and (b%2==0):
#     print('두 수 모두 짝수입니다')
# if (a%2==0) or (b%2==0):
#     print('두 수 중 하나 이상이 짝수입니다')
# #LAB 3-4: 복합 조건식의 이해
# #1
# num=2
# if 1<= num <=10:
#     print(True)
# else:
#     print()
# #2
# age=18
# if 10<= age < 19:
#     print('청소년 입니다')

# #코드 3-14 : 윤년을 판별하기 위한 코드
# year = int(input('연도를 입력하세요 : '))
# is_leap_year=((year % 4 ==0) and (year % 100 != 0) or (year % 400 == 0))
# print(year, '년은 윤년입니다?', is_leap_year)

# # 3.4 if-elif-else 문
# score= int(input('점수를 입력하세요 : '))
# if score >= 90:
#     grade = 'A'
# if score < 90 and score >= 80:
#     grade = 'B'
# if score < 80 and score >= 70:
#     grade= 'C'
# if score < 70 and score >= 60:
#     grade= 'D'
# if score < 60:
#     grade = 'F'
# print('당신의 등급은 :', grade)

# #코드 3-16: 'A','B','C','D','F' 등급 계산을 위한 복합 if 문
# score= int(input('점수를 입력하세요 : '))
# if score >=90:
#     grade = 'A'
# else:
#     if score >=80:
#         grade='B'
#     else:
#         if score >= 70:
#             grade= 'C'
#         else:
#             if score >= 60:
#                 grade= 'D'
#             else:
#                 grade='F'
# print('당신의 등급은 :', grade)
#코드 3-17: if-elif-else 문으로 구성된 등급계산기
# score= int(input('점수를 입력하세요 : '))
# if score >= 90:
#     grade='A'
# elif score>=80:
#     grade='B'
# elif score>=70:
#     grade='C'
# elif score >=60:
#     grade ='D'
# else:
#     grade= 'F'
# print('당신의 등급은 :', grade)

#lab 3-5 :if-elif-else 문을 사용한 다중 조건식
#1
# a=int(input('자동차의 속도를 입력하세요(단위 : km/h ): '))
# if a>=100:
#     print('고속')
# elif 60 <= a <=100:
#     print('중속')
# elif a<60:
#     print('저속')
# #2
# b=int(input('미세먼지 농도를 입력하세요(단위 : microgram/m^3): '))
# if b>=76:
#     print('매우 나쁨')
# elif 36<=b <=75:
#     print('나쁨')
# elif 16<=b<=35:
#     print('보통')
# else:
#     print('좋음')

#for 반복문

#코드 3-18 : print() 함수의 호출을 통한 반복적 수행
print('Welcome to everyone!!')
print('Welcome to everyone!!')
print('Welcome to everyone!!')
print('Welcome to everyone!!')
print('Welcome to everyone!!')
#코드 3-19 : for 문을 이용한 반복적 수행
for i in range(5):
    print('Welcome to everyone!!')
#루프 제어변수의 익명화
for _ in range(10):
    print('Welcome to everyone!!!') 
#실행문에서 사용되지 않는 i같은 루프변수는 언더스코어(_) 대신 넣어서 익명화 시킬 수 있음
#코드 3-20 : for 문을 이용한 반복적 수행 - 10회 수행
for i in range(10):
    print(i, 'Welcome to everyone!!') #0 Welcome to everyone!! 0-9까지 숫자별로 출력
#lab 3-6 :반복문을 이용해서 코드 작성
#1
for _ in range(5):
    print('Hello, Python!')
#2
for _ in range(5):
    print(_)

#range() 함수의 활용과 리스트 - range(시작,끝(제외),증가 되는 수)
print(list(range(5))) #[0, 1, 2, 3, 4]
print(list(range(0,5,2))) #[0, 2, 4]
print(list(range(2,5))) #[2, 3, 4]
print(range(-2,-10,-2)) #range(-2, -10, -2)

#LAB 3-7: range() 함수의 응용
#1
print(list(range(1,100+1))) #[1,2,3,4,5 (생략),100]
#2
print(list(range(2,100+1,2))) #1 이상 100 이하의 짝수 리스트 생성
print(list(range(1,100+1,2))) #1 이상 100 이하의 홀수 리스트 생성
print(list(range(-100,0))) #-100 보다 크고 0 보다 작은 음수 리스트
