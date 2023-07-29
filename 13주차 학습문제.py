#2
import random as r
nn=[]
for _ in range(10):
    num=r.randrange(1,100)
    nn.append(num)
hap=0
for i in range(10):
    num=nn[i]
    hap=num
print(hap)
#4
arr1=[1,2,3,4]
arr2=[]
for i in range(3,-1,-1):
    arr2.append(arr1[i])
print(arr1)
print(arr2)
#5
n=list(map(int,input('입력 :').split()))
print('정렬 전 :',n)
n.sort()
print('정렬 후 :',n)
nn=[]
for i in n:
    nn.append(oct(i))
n2=" ".join(nn)
print('8진수 변환 :',n2)
#6
import random as r
a=r.randint(1,100)
count=0
while True:
    q=int(input('숫자 입력 :'))
    count+=1
    if q==a:
        print(f'정답 . 축하. {count}번 만에 맞춤')
        break
    elif q>a:
        print('좀 더 낮춰라')
        continue
    else:
        print('좀 더 높여라')
        continue