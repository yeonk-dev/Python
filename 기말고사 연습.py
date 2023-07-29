#9주차 8번
s=0
hap=1234
while (hap<4568):
    if hap%444==0:
        s=hap+s
    hap=hap+1
print(s)

#9번
s=0
for i in range(1,10000):
    if i%555==0:
        s=s+i
        if s>100000:
            break
        else:
            continue
print('555배수의 합계는:',s) #555배수의 합계는: 94905
print('반복문 블록의 반복 횟수는 :',i) #반복문 블록의 반복 횟수는 : 9999

#10주차 2번
def plus(a,b,c):
    result=0
    result=a+b+c
    return result
hap=plus(100,200,300)
print(hap) #600
#4번
# a,b=(map(float,input('두 수를 입력하시오 :').split()))
# def num(a,b):
#     print(f'{a}+{b}={a+b}')
#     print(f'{a}-{b}={a-b}')
#     print(f'{a}*{b}={a*b}')
#     print(f'{a}/{b}={a/b}')
# num(a,b)

#5번 
# num=int(input('임의의 자연수를 입력하세요 : '))
# def 완전수(num):
#     result=0
#     for i in range(1,num):
#         if num%i==0:
#             result=result+i
#         else:
#             continue
#     if result==num:
#         print(f'{num}은 완전수 입니다.')
#     else:
#         print(f'{num}은 완전수가 아닙니다.')
# 완전수(num)
# #6
# def pic_out(n):
#     for i in range(n):
#         print("#",end='')
#     print()
# num=input('여러 개의 숫자를 입력하시오:')
# for n in num:
#     pic_out(int(n))

#13주차 2번
import random as r
nn=[]
for _ in range(10):
    num=r.randrange(1,100)
    nn.append(num)
hap=0
for i in range(10):
    num=nn[i]
    hap+=num
print(hap)

#4번
arr1=[1,2,3,4]
arr2=[]
for i in range(3,-1,-1):
    arr2.append(arr1[i])
print(arr1)
print(arr2)
#5
n=list(map(int, input('입력 :').split()))
print('정렬 전 :',n)
n.sort()
print('정렬 후 :',n)
nn=[]
for i in n:
    nn.append(oct(i))
n2=" ".join(nn)
print(n2)
