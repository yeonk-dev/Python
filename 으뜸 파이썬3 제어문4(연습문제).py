3.1
print(100 > 200) #False
print(100 >= 200) #False
print(100<200) #True
print(100<=200) #True
print(100==200) #False
print(100 !=200) #True
print(200==200) #True
print(200 != 200) #False
print(True or True) #True
print(True or False) #True
print(True and False) #False
print(True or True and False) #True
print(True and True or False) #True
print('Morning' < 'morning') #True
print('A' > 'B') #False
3-2
name=str(input('이름을 입력하세요 : '))
hieght=int(input('키를 입력하시오 : '))
if hieght> 140:
    print(f'{name}님은 놀이기구를 탈 수 있습니다')
else:
    print(f'{name}님은 놀이기구를 탈 수 없습니다')
3-3
age=int(input('나이를 입력하시오 : '))
height=int(input('키를 입력하시오(단위 cm) : '))
if age >=19 and height>=150:
    print('입장할 수 있습니다')
else:
    print('입장할 수 없습니다')
3.4
age=int(input('나이를 입력하시오 : '))
if age>=20:
    print('Adult')
elif 10<= age < 20:
    print('Youth')
else:
    print('Kid')
3.5
a,b=map(int,input('두 정수를 입력하시오 : ').split())
a,b=input('두 정수를 입력하시오 : ').split()
a=int(a)
b=int(b)
if a>b:
    print(a,b)
else:
    print(b,a)
3.6
a=int(input())
b=int(input())
c=int(input())
a,b,c=input('세 정수를 입력하시오:').split()
a=int(a)
b=int(b)
c=int(c)
# print('세 정수를 입력하시오 : ',a,b,c)
if a>b>c:
    print(c,b,a)
elif a>c>b:
    print(b,c,a)
elif b>a>c:
    print(c,a,b)
elif b>c>a:
    print(a,c,b)
elif c>a>b:
    print(b,a,c)
else:
    print(a,b,c)
3.7
game_score=int(input('게임점수를 입력하시오 : '))
if game_score>=1000:
    print('고수입니다')
else:
    print('입문자입니다')
3.8
x,y=map(int,input('점의 좌표 x,y를 입력하시오 :').split())
if x>0 and y>0:
    print('1사분면에 있음')
elif x<0 and y<0:
    print('2사분면에 있음')
elif x<0 and y<0:
    print('3사분면에 있음')
else:
    print('4사분면에 있음')
3.9
i=int(input('정수를 입력하시오:'))
if i%2==0:
    print(f'{i}는 2로 나누어 집니다')
else:
    print(f'{i}는 2로 나누어 지지 않습니다')
if i%3==0:
    print(f'{i}는 3로 나누어 집니다')
else:
    print(f'{i}는 3로 나누어 지지 않습니다')
if i%2==0 and i%3==0:
    print(f'{i}는 2와 3모두로 나누어집니다')
else:
    print(f'{i}는 2와 3 모두로 나누어지지 않습니다')


3.10
a,b=map(int,input('두 정수를 입력하시오 : ').split())
if a%b==0:
    print(f'{a}는 {b}의 배수입니다.')
else:
    print(f'{b}는 {a}의 배수가 아닙니다.')

3.11
(1)
a,b,c=map(int, input('세 복권번호를 입력하시오 : ').split())
d=0  
if a==2 or b==2 or c==2:
    d+=1
if a==3 or b==3 or c==3:
    d+=1
if a==9 or b==9 or c==9:
    d+=1

if d==3:
    print('1억원')
elif d==2:
    print('1천만 원')
elif d==1:
    print('1만원')
else:
    print('다음 기회에')
#3.12
x,y=map(int,input('점의 좌표 x,y를 입력하시오 : ').split())
if -5<x<5 and -5<y<5:
    print('원의 내부에 있음')
else:
    print('원의 외부에 있음')

(2) random 모듈 사용
import random as r
x,y,z=2,5,9
luck=[x,y,z]
ax,ay,az=map(int,input('세 복권번호를 입력하시오').split())
answer=[ax,ay,az]
lucknum=0
for i in answer:
    if i in luck:
        lucknum+=1
if lucknum==3:
    print('1억원')
elif lucknum==2:
    print('1천만원')
elif lucknum==1:
    print('1만원')
else:
    print('다음기회에')
3.13
import math as m       
x,y=map(int,input('점의 좌표,x,y를 입력하시오').split(' '))
#r=int(((x-3)**2+(y-4)**2)**0.5)
r=m.sqrt(((x-3)**2+(y-4)**2))
if r>10:
    print('원의 외부에 있음')
else:
    print('원의 내부에 있음')
x,y=map(int,input('점의 좌표,x,y를 입력하시오').split(' '))
r=int(((x-3)**2+(y-4)**2)**0.5)
if r>10:
    print('원의 외부에 있음')
else:
    print('원의 내부에 있음')


3.14
a=str(input('알파벳을 입력하시오 :'))
for b in a:
   if b in ['a','e','i','o','u']:
       print(f'{b}는 모음입니다')
   else:
       print(f'{b}는 자음입니다')
3.15
a=2 
for i in range(1,10):
    print(f'{a}*{i}={a*i}')

a=2 
i=1
while i<10:
    print(f'{a}*{i}={a*i}')
    i+=1 

3.16
num=int(input('1에서 9까지의 수를 입력하세요 :'))

for i in range(1,10,1):
    if num <10 and num >0:
        print(f'{num}*{i}={num*i}')
    else:
        num=int(input('다시 1에서 9까지의 수를 입력하세요 :'))
        continue

#2 while 문 
while True:
    num=int(input('1에서 9까지의 수를 입력하세요 :'))
    if num<10:
        for i in range(1,10):
            print(f'{num}*{i}={num*i}')
    else:
        num=int(input('1에서 9까지의 수를  다시 입력하세요 :'))
        continue
        
        

3.17
(1) for i in range(3):
    print('Python')
    print('is ')
    print('FUN!') #SyntaxError: invalid syntax
(2)for i in range(3):
    print('Python ')
    print('is ')
print('FUN!') #SyntaxError: invalid syntax
(3) for i in range(3):
         print('python ')
    print('is ')
    print('FUN! ')

3.18
print('''
맛나식당에 온것을 환영합니다. 메뉴는 다음과 같습니다
1) 햄버거
2) 치킨
3) 피자
      '''.strip())
menu={'1':'치킨','2':'햄버거','3':'피자'}
answer=''
answer=input('1에서 3까지의 메뉴를 선택하세요 :')
while(True):
    if answer not in list(menu.keys()):
        while(True):
            answer=input('메뉴를 다시입력하세요 :')
            if answer in list(menu.keys()):
                break
    else:
        break
value=menu.get(answer)
print(f'{value}을 선택했습니다.')
3.19
print('''
맛나식당에 온것을 환영합니다. 메뉴는 다음과 같습니다
- 햄버거(입력b)
- 치킨(입력c)
- 피자(입력 p)
      '''.strip())
menu={'c':'치킨','b':'햄버거','p':'피자'}
answer=''
answer=input('메뉴를 선택하세요 : ')
while(True):
    if answer not in list(menu.keys()):
        while(True):
            answer=input('메뉴를 다시입력하세요(알파벳 b,c,p입력)')
            if answer in list(menu.keys()):
                break
    else:
        break
value=menu.get(answer)
print(f'{value}을 선택했습니다.')
3.20
(1) 
n=int(input('숫자를 입력하세요:'))
for i in range(1,n+1):
   print(' '*(n-i),'*'*i)
(2) 이중for문 사용
n=int(input('숫자를 입력하세요:'))
for i in range(1,n+1):
   for j in range((n-i)):
       print(' ',end='')
   for k in range(i):
       print('*',end='')
   print()

3.21
a=int(input('숫자를 입력하세요 :'))
b=0
for i in range(2,a):
   if (a%i==0):
       b=1
   else:
       continue
if b==0:
   print(f'{a}은 소수입니다')
else:
   print(f'{a}은 소수가 아닙니다')

3.22
for i in range(2,12+1):
    b=0
    for j in range(2,i):
        if i%j==0:
            b=1
        else:
            continue
    if b==0:
        print(f'{i}: 소수')
    else:
        print(f'{i}: 합성수')

3.23
n=int(input('숫자를 입력하세요 :'))
sum=0
for i in range(1,n+1):
   sum+=i*i
print(f'결과는 {sum}입니다')  
3.24 
n=int(input('숫자를 입력하세요:'))
sum=0
for i in range(1,n+1):
    sum+=(1/i)*(1/i)
print(f'결과는 {sum}입니다')
3.25
우물의깊이=30
날=1
올라간높이=0
하루에올라가는높이=7
밤에미끄러지는높이=5
while(True):
   if 우물의깊이<=올라간높이:
       break
   elif 날==1:
       올라간높이+=하루에올라가는높이 #day1은 하루에 7미터 오르고 바로 다음 2일로 넘어감
   else:
       올라간높이+=하루에올라가는높이#즉 잘때,day2부터 5미터 미끄러지고 다시 7미터 오름.
       올라간높이-=밤에미끄러지는높이
   print(f'day : {날}  달팽이의 위치 : {올라간높이} 미터')
   날+=1
print(f'우물을 탈출하는 데 걸린 날은 {날-1}일 입니다')

3.26
n=int(input('입력 : '))
for i in range(1,n+1):
    if (i%2==1):
        for j in range(n*(i-1)+1,n*(i)+1):
            print(f'{j}\t',end='')
        print()
    else:
        for j in range(n*(i),n*(i-1),-1):
            print(f'{j}\t',end='')
        print()
3.27
a=[]
for i in range(100,1000):
   if (i//100)**3+(i%100//10)**3+(i%10)**3==i:
      a.append(i)
   else:
      continue
print('세 자리의 암스트롱 수:',str(a)[1:-1].replace(',',''))
3.28
num=int(input('정수를 입력하세요:')) 
num_1=int(str(num)[::-1])
if num==num_1:
   print(f'{num}는 거꾸로 정수입니다')
else:
   print(f'{num}는 거꾸로 정수가 아닙니다')
3.29
oil=500
while True:
    oil_n=int(input('충전 또는 사용한 연료를 +/- 기호와 함께 입력하세요 : '))
    oil=oil+oil_n
    print(f'현재 탱크량은 {oil}입니다')
    if oil<50:
        print('경고: 연료가 10% 미만이니 충전하세요!')
        break 
3.30
print('1)덧셈 2)뺄셈 3)곱셈 4)나눗셈')
num=int(input('어떤 연산을 원하는지 번호를 입력하세요: '))
print('연산을 원하는 숫자 두개를 입력하세요')
a=int(input())
b=int(input())
if num==1:
   print(f'{a}+{b}={a+b}')
elif num==2:
   print(f'{a}-{b}={a-b}')
elif num==3:
   print(f'{a}*{b}={a*b}')
elif num==4:
   print(f'{a}/{b}={a/b}')
else:
   print('잘못 입력하셨습니다')

#3.31
#1. 첫번째 진약수를 구해서 전부 더함
#2. 첫번째 진약수를 몽땅 더한 수의 진약수를 구해서 또 몽땅 더함
#3. 둘의 진약수합이 서로를 가리키면 출력 아니면 패스
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



 


