#2
def plus(v1,v2,v3):
    result=0
    result=v1+v2+v3
    return result
hap=plus(100,200,300)
print(hap)
#4
def number(a,b):
    print(f'{a}+{b}={a+b}')
    print(f'{a}-{b}={a-b}')
    print(f'{a}*{b}={a*b}')
    print(f'{a}/{b}={a/b}')
number(a,b)

#5
num=int(input('임의의 자연수를 입력하시오: '))
result=0

for i in range(1,num):
    if num%i==0:
        result+=i
    else:
        continue

divisor=[i for i in range(1,num) if num%i==0]

if result==num:
    print(f'{num}은 완전수 입니다')
else:
    print(f'{num}은 완전수가 아닙니다.')
#함수 사용
def 완전수(num):
    result=0
    for i in range(1,num):
        if num%i==0:
            result+=i
        else:
            continue
    if result==num:
        print(f'{num}은 완전수 입니다')
    else:
        print(f'{num}은 완전수가 아닙니다.')
완전수(num)

#다른 방법
def per_num(a):
    s=0
    n=int(a*0.5)
    for i in range(1,n+1):
        if a%i==0:
            s=s+i
        return s
a=int(input('임의의 자연수를 입력하시오:'))
if a==per_num(a):
    print(f'{a}는 완전수 입니다.')
else:
    print(f'{a}는 완전수가 아닙니다.')

#6
def a(n):
    for i in range(0,len(n)):
        for j in range(1,int(n[i])+1):
            print("#",end=" ")
        print("")

b=list(input())
a(b)

#다른 정답 6번
def pic_out(n):
    for i in range(n):
        print("#",end='')
    print()
num=input('여러 개의 숫자를 입력하시오:')
for n in num:
    pic_out(int(n))