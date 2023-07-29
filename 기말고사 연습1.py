# a,b,c=map(int,input('세 정수 입력 :').split())
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

# game=int(input('게임점수를 입력하시오 :'))
# if game>=1000:
#     print('고수입니다.')
# else:
#     print('입문자입니다.')

# x,y=map(int,input('점의 좌표 x,y를 입력하시오 :').split())
# if x>0 and y>0:
#     print('1사분면에 있음')
# elif x<0 and y>0:
#     print('2사분면에 있음')
# elif x<0 and y<0:
#     print('3사분면에 있음')
# else:
#     print('4사분면에 있음')

# num=int(input('정수를 입력하시오 :'))
# if num%2==0:
#     print(f'{num}은 2로 나누어집니다')
# else:
#     print(f'{num}은 2로 나누어지지 않습니다')
# if num%3==0:
#     print(f'{num}은 3로 나누어집니다')
# else:
#     print(f'{num}은 3로 나누어지지 않습니다')
# if num%2==0 and num%3==0:
#     print(f'{num}은 2와 3모두로 나누어집니다.')
# else:
#     print(f'{num}은 2와 3모두로 나누어지지 않습니다.')

# a,b=map(int,input('두 정수를 입력 :').split())
# if a%b==0:
#     print(f'{a}는 {b}의 배수입니다.')
# else:
#     print(f'{b}는 {a}의 배수가 아닙니다')

# a,b,c=map(int,input('세 복권번호를 입력하시오 :').split())
# d=0
# if a==2 or b==2 or c==2:
#     d+=1
# if a==3 or b==3 or c==3:
#     d+=1
# if a==9 or b==9 or c==9:
#     d+=1

# if d==0:
#     print('다음 기회에..')
# elif d==1:
#     print('상금 1만원')
# elif d==2:
#     print('상금 1천만 원')
# else:
#     print('상금 1억원')

# x,y=map(int,input('점의 좌표 x,y를 입력하시오 :').split())
# if (((x*x)+(y*y))**0.5)>=5:
#     print('원의 외부에 있음')
# else:
#     print('원의 내부에 있음')

# x,y=map(int,input('점의 좌표 x,y를 입력하시오 :').split())
# if ((((x-3)**2+(y-4)**2))**0.5)>=10:
#     print('원의 외부에 있음')
# else:
#     print('원의 내부에 있음')

# alpa=input('알파벳을 입력하시오 :')
# a=['a','e','i','o','u']
# if alpa in a:
#     print(f'{alpa}는 모음입니다.')
# else:
#     print(f'{alpa}는 자음입니다')

# for i in range(1,10):
#     print(f'2*{i}={2*i}')
# i=1
# while i<10:
#     print(f'2*{i}={2*i}')
#     i+=1

# num=int(input('1에서 9까지의 수를 입력하세요:'))
# for i in range(1,10):
#     if 1<=num<=9:
#         print(f'{num}*{i}={num*i}')
#     else:
#         num=int(input('1에서 9까지의 수를 다시 입력하세요:'))
#         continue

# num=int(input('1에서 9까지의 수를 입력하세요 :'))

# for i in range(1,10,1):
#     if num <10 and num >0:
#         print(f'{num}*{i}={num*i}')
#     else:
#         num=int(input('다시 1에서 9까지의 수를 입력하세요 :'))
#         continue

# #2 while 문 
# while True:
#     num=int(input('1에서 9까지의 수를 입력하세요 :'))
#     if num<10:
#         for i in range(1,10):
#             print(f'{num}*{i}={num*i}')
#     else:
#         continue

# print('''
# 맛나식당에 온것을 환영합니다. 메뉴는 다음과 같습니다
# 1) 햄버거
# 2) 치킨
# 3) 피자
#       '''.strip())
# menu={'1':'치킨','2':'햄버거','3':'피자'}
# answer=''
# answer=input('1에서 3까지의 메뉴를 선택하세요 :')
# while(True):
#     if answer not in list(menu.keys()):
#         while(True):
#             answer=input('메뉴를 다시입력하세요 :')
#             if answer in list(menu.keys()):
#                 break
#     else:
#         break
# value=menu.get(answer)
# print(f'{value}을 선택했습니다.')

# n=int(input('숫자 입력 :'))
# for i in range(1,1+n):
#     for j in range(n-i):
#         print(' ',end='')
#     for k in range(i):
#         print("*",end='')
#     print()

# n=int(input('숫자 입력 :'))
# b=0
# for i in range(2,n):
#     if n%i==0:
#         b+=1
#     else:
#         continue
# if b==0:
#     print(f'{n}은 소수입니다')
# else:
#     print(f'{n}은 소수가 아닙니다')

# for i in range(2,13):
#     b=0
#     for j in range(2,i):
#         if i%j==0:
#             b+=1
#         else:
#             continue
#     if b==0:
#         print(f'{i} : 소수')
#     else:
#         print(f'{i} : 합성수')

# num=int(input('숫자 입력'))
# sum=0
# for i in range(1,num+1):
#     sum+=i*i
# print(f'결과는 {sum}입니다.')
    
# num=int(input('숫자 입력'))
# sum=0
# for i in range(1,num+1):
#     sum+=1/(i*i)
# print(f'결과는 {sum}입니다.')

# n=int(input('입력:'))
# for i in range(1,n+1):
#     if i%2==1:
#         for j in range(n*(i-1)+1,n*(i)+1):
#             print(f'{j}\t',end='')
#         print()
#     else:
#         for j in range(n*(i),n*(i-1),-1):
#             print(f'{j}\t',end='')
#         print()
# s=[]
# for i in range(100,1000):
#     if ((i//100)**3)+(((i%100)//10)**3)+(((i%10)**3))==i:
#         s.append(i)
#     else:
#         continue
# print('세 자리의 암스트롱 수:',str(s)[1:-1].replace(',',''))

# num=int(input('정수를 입력하세요:')) 
# num_1=int(str(num)[::-1])
# if num==num_1:
#    print(f'{num}는 거꾸로 정수입니다')
# else:
#    print(f'{num}는 거꾸로 정수가 아닙니다')

# oil=500
# while(True):
#     plus=int(input('충전 또는 사용한 연료를 +/-기호와 함께 입력하십시오 :'))
#     oil=oil+plus
#     print(f'현재 탱크량은 {oil} 입니다.')
#     if oil<50:
#         print(f'현재 탱크량은 {oil} 입니다.')
#         print('경고! 연료가 10% 미만이니 충전하세요!')
#         break

# print('1)덧셈 2)뺄셈 3)곱셈 4)나눗셈')
# a=int(input('어떤 연산을 원하는지 번호를 입력하세요 : '))
# if a==0 or a>5:
#     print('잘못 입력하셨습니다.')
# else:
#     print('연산을 원하는 숫자 두개를 입력하세요:')
#     x=int(input())
#     y=int(input())
#     if a==1:
#         print(f'{x}+{y}={x+y}')
#     elif a==2:
#         print(f'{x}-{y}={x-y}')
#     elif a==3:
#         print(f'{x}*{y}={x*y}')
#     elif a==4 :
#         print(f'{x}/{y}={x/y}')

# i2=0
# for i in range(1,20001):
#     sum1=0
#     sum2=0
#     for j in range(1,i):
#         if i%j==0:
#             if j==i:
#                 continue
#             else:
#                 sum1+=j
#         else:
#             continue
#     i2=sum1
#     for k in range(1,i2):
#         if i2%k==0:
#             if k==i2:
#                 continue
#             else:
#                 sum2+=k
#         else:
#             continue
# if i==sum2:
#     print(f'{i}의 친화수 {i2}')

sum1=0#첫번째수의 진약수의 합
sum2=0#첫번째수의 진약수의 합(i2)의 진약수들의 합
i2=0

for i in range(1,20000+1):
    sum1=0
    sum2=0
    for j in range(1,i):
        if i%j==0:
            if j==i:
                continue
            else:
                sum1+=j
        else:
            continue
    
    i2=sum1
    for k in range(1,i2):
        if i2%k==0:
            if k==i2:
                continue
            else:
                sum2+=k
        else:
            continue
    if i==sum2:
        print(f'{i}의 친화수 {i2}') 

    
    


