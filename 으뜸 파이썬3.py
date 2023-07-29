#3.1
# print(100 > 200) #False
# print(100 >= 200) #False
# print(100<200) #True
# print(100<=200) #True
# print(100==200) #False
# print(100 !=200) #True
# print(200==200) #True
# print(200 != 200) #False
# print(True or True) #True
# print(True or False) #True
# print(True and False) #False
# print(True or True and False) #True
# print(True and True or False) #True
# print('Morning' < 'morning') #True
# print('A' > 'B') #False
#3-2
# name=str(input('이름을 입력하세요 : '))
# hieght=int(input('키를 입력하시오 : '))
# if hieght> 140:
#     print(f'{name}님은 놀이기구를 탈 수 있습니다')
# else:
#     print(f'{name}님은 놀이기구를 탈 수 없습니다')
#3-3
# age=int(input('나이를 입력하시오 : '))
# height=int(input('키를 입력하시오(단위 cm) : '))
# if age >=19 and height>=150:
#     print('입장할 수 있습니다')
# else:
#     print('입장할 수 없습니다')
#3.4
# age=int(input('나이를 입력하시오 : '))
# if age>=20:
#     print('Adult')
# elif 10<= age < 20:
#     print('Youth')
# else:
#     print('Kid')
#3.5
# a,b=map(int,input('두 정수를 입력하시오 : ').split())
# if a>b:
#     print(a,b)
# else:
#     print(b,a)
#3.6
# a,b,c=map(int,input('세 정수를 입력하시오:').split())
# if a>b>c:
#     print(c,b,a)
# elif a>c>b:
#     print(b,c,a)
# elif b>a>c:
#     print(c,a,b)
# elif b>c>a:
#     print(a,c,b)
# elif c>a>b:
#     print(b,a,c)
# else:
#     print(a,b,c)
#3.7
# game_score=int(input('게임점수를 입력하시오 : '))
# if game_score>=1000:
#     print('고수입니다')
# else:
#     print('입문자입니다')
#3.8
# x,y=map(int,input('점의 좌표 x,y를 입력하시오 :').split())
# if x>0 and y>0:
#     print('1사분면에 있음')
# elif x<0 and y<0:
#     print('2사분면에 있음')
# elif x<0 and y<0:
#     print('3사분면에 있음')
# else:
#     print('4사분면에 있음')
#3.9
# i=int(input('정수를 입력하시오:'))
# if i%2==0:
#     print(f'{i}는 2로 나누어 집니다')
# else:
#     print(f'{i}는 2로 나누어 지지 않습니다')
# if i%3==0:
#     print(f'{i}는 3로 나누어 집니다')
# else:
#     print(f'{i}는 3로 나누어 지지 않습니다')
# if i%2==0 and i%3==0:
#     print(f'{i}는 2와 3모두로 나누어집니다')
# else:
#     print(f'{i}는 2와 3 모두로 나누어지지 않습니다')


#3.10
# a,b=map(int,input('두 정수를 입력하시오 : ').split())
# if a%b==0:
#     print(f'{a}는 {b}의 배수입니다.')
# else:
#     print(f'{b}는 {a}의 배수가 아닙니다.')

#3.11
# a=int(input())
# b=int(input())
# c=int(input())
# a,b,c=map(int, input('세 복권번호를 입력하시오 : ').split())
# d=0  - 걸릴 확률
# if a==2 or b==2 or c==2:
#     d+=1
# elif a==3 or b==3 or c==3:
#     d+=1
# elif a==9 or b==9 or c==9:
#     d+=1

# if d==3:
#     print('1억원')
# elif d==2:
#     print('1천만 원')
# elif d==1:
#     print('1만원')
# else:
#     print('다음 기회에')
#3.12
# x,y=map(int,input('점의 좌표 x,y를 입력하시오 : ').split())
# if -5<x<5 and -5<y<5:
#     print('원의 내부에 있음')
# else:
#     print('원의 외부에 있음')

#3.13
# import math as m       
# x,y=map(int,input('점의 좌표,x,y를 입력하시오').split(' '))
# #r=int(((x-3)**2+(y-4)**2)**0.5)
# r=m.sqrt(((x-3)**2+(y-4)**2))
# if r>10:
#     print('원의 외부에 있음')
# else:
#     print('원의 내부에 있음')


#3.14
#a=str(input('알파벳을 입력하시오 :'))
#for b in a:
#    if b in ['a','e','i','o','u']:
#        print(f'{b}는 모음입니다')
#    else:
#        print(f'{b}는 자음입니다')