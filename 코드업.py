#코드업 6020번
# a,b = input().split('-')
# print(a,b,sep='')

# #코드업6022번
# s = input()
# print(s[0:2], s[2:4], s[4:6], sep=' ')

# #코드업6023번
# h, m, s = input().split(':')
# print(m)

# #코드업6024번
# a,b=input().split()
# s=a+b
# print(s)

# #코드업6011번
# f=input()
# f=float(f)
# print(f)

#코드업6025번
# a,b=input().split()
# c=int(a)+int(b)
# print(c)

# #코드업6026번
# a,b=input().split()
# c=float(a)+float(b)
# print(c)

#코드업6027번
# a = input()
# n = int(a)          
# print("%x"%a)

#코드업1151번
# n=int(input())
# if n<10:
#     print("small")
# else:
#     print("")

# #코드업1070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)
# n=int(input("몇 월 입니까?:"))
# if 12<= n<= 2:
#     print("겨울")
# elif 3 <=n <= 5:
#     print("봄")
# elif 6 <=n<= 8:
#     print("여름")
# elif 9 <=n <= 11:
#     print("가을")

# #코드업1152 : 10보다 작은 수 (else 버전)
# g=int(input())
# if g <10:
#     print("small")
# else:
#     print("big")

#코드업1153 : 두 수의 대소 비교
# a,b=input().split()
# if a>b:
#     print(">")
# elif a<b:
#     print("<")
# elif a==b:
#     print("=")

#코드업1154 : 큰수 - 작은수
# a,b=input().split()
# if a>b:
#     print(a-b)
# elif a<b:
#     print(b-a)
# a,b=map(int,input().split())
# if a>b:
#     print(a-b)
# elif a<b:
#     print(b-a)

#코드업1155 : 7의 배수
# from sys import stdin

# num=int(stdin.readline)
# if num%7==0:
#     print("multiple")
# else:
#     print("not multiple")

#코드업1156 : 홀수 짝수 구별
# num=int(input())
# if num%2==1:
#     print("odd")
# else:
#     print("even")

#코드업1157특별한 공 던지기 1
#50이상 60이하이면 win을 출력, 그 외에는 lose를 출력하시오.
# num=int(input())
# if 50<=num<=60:
#     print("win")
# else:
#     print("lose")

#코드업1158 : 특별한 공 던지기 2
# num=int(input())
# if 30<=num<=40:
#     print("win")
# elif 60<=num<=70:
#     print("win")
# else:
#     print("lose")

#코드업1159 : 특별한 공 던지기 3
# num=int(input())
# if 50<=num<=70:
#     print("win")
# elif num%6==0:
#     print("win")
# else:
#     print("lose")
#코드업1160 : 아르바이트 가는 날

#코드업1161 : 홀수와 짝수 그리고 더하기
# a,b=input().split()
# c=a+b
# if a%2==0:
#     print("짝수")
# else:
#     print("홀수")
# if b%2==0:
#     print("짝수")
# else:
#     print("홀수")
# if c%2==0:
#     print("짝수")
# else:
#     print("홀수")
# print("{}+{}={}".format(a,b,c))
# def honzak():
#     n1=int(input('첫번째 정수'))
#     n2=int(input('두번째 정수'))
#     if(n1%2==1):
#         if(n2%2==1):
#             print('홀수+홀수=짝수')
#         else:
#             print('홀수+짝수=홀수')
#     else:
#         if(n2%2==1):
#             print('짝수+홀수=홀수')
#         else:
#             print('짝수+짝수=짝수')
# honzak()

#코드업 1162 : 당신의 사주를 봐 드립니다 1
# a,b,c=input().split()
# d=int(a)-int(b)+int(c)
# if d%2==0:
#     print("대박")
# else:
#     print("그럭저럭")

# a,b,c =map(int.input().split())
# if (a-b+c)%10==0:
#     print("대박")
# else:
#     print("그럭저럭")

#코드업 1163 : 당신의 사주를 봐 드립니다 2
# a,b,c =map(int,input().split())
# if ((a+b+c)//100)%2==0:
#     print("대박")
# else:
#     print("그럭저럭")

#코드업 1164 : 터널 통과하기 1
car=list(map(int,input().split()))
if min(car)<=170:
    print("CRUSH")
else:
    print("PASS")
