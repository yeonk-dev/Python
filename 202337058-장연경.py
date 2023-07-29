#4.1
def my_greet():
    print('환영합니다.')
my_greet()
my_greet()
# #4.2
def square(n):
    return n*n
print('3의 제곱은: ',square(3))
print('4의 제곱은: ',square(4))
# #4.3
def max2(m,n):
    if m>n:
        return m
    else:
        return n
def min2(m,n):
    if m>n:
        return n
    else:
        return m
print('100과 200중 큰 수는:',max2(100,200))
print('100과 200중 작은 수는:',min2(100,200))
# #4.4
def mile2km(m):
    for m in range(1,6,1):
        print(m,'마일=',m*1.61,'킬로미터' )
mile2km(1)
# #4.5
def inch2km(cm):
    for cm in range(1,6,1):
        print(cm,'인치=',cm*2.54,'센티미터' )
inch2km(1)
# #4.6
def cel2fah(cel):
    for cel in range(10,51,10):
        print('섭씨',cel,'도= 화씨',(9/5)*cel+32,'도')
cel2fah(10)
#4.7
def mean3(a,b,c):
    return (a+b+c)/3
def max3(a,b,c):
    return max(a,b,c)
def min3(a,b,c):
    return min(a,b,c)
a,b,c=map(int,input('세 수를 입력하시오:').split())
print(f'{a},{b},{c}의 평균값은',mean3(a,b,c))
print(f'{a},{b},{c}의 최대값은',max3(a,b,c))
print(f'{a},{b},{c}의 최소값은',min3(a,b,c))

#4.8
#1 (내장 함수 사용)
def mean3(a,b,c,d,e,f):
    return (a+b+c+d+e+f)/6
def max3(a,b,c,d,e,f):
    return max(a,b,c,d,e,f)
def min3(a,b,c,d,e,f):
    return min(a,b,c,d,e,f)
a,b,c,d,e,f=map(int,input('여섯 개의 수를 입력하시오:').split())
print(f'평균값은','{:.1f}'.format(mean3(a,b,c,d,e,f)))
print(f'최대값은',max3(a,b,c,d,e,f))
print(f'최소값은',min3(a,b,c,d,e,f))
#2 (함수 생성)
def mean3(a,b,c,d,e,f):
    return (a+b+c+d+e+f)/6
def max3(a,b,c,d,e,f):
    max_val=int(num[0])
    for i in num:
        if max_val<int(i):
            max_val=int(i)
    return max_val
def min3(a,b,c,d,e,f):
    min_val=int(num[0])
    for i in num:
        if min_val>int(i):
            min_val=int(i)
    return min_val
a,b,c,d,e,f=map(int,input('여섯 개의 수를 입력하시오:').split())
print(f'평균값은','{:.1f}',format(mean3(a,b,c,d,e,f)))
print(f'최대값은',max3(a,b,c,d,e,f))
print(f'최소값은',min3(a,b,c,d,e,f))
#4.9
#1 (내장 함수 사용)
def mean_of_n(nums):
    result=0
    for num in nums:
        result+=num
    r1=result/len(nums)
    return r1
def max_of_n(nums):
    return max(nums)
def min_of_n(nums):
    return min(nums)
nums=list(map(int,input('정수를 여러 개 입력하시오:').split(' ')))
print('평균값은:','{:.1f}',format(mean_of_n(nums)))
print('최댓값은:',max_of_n(nums))
print('최소값은:',min_of_n(nums))
#2 (함수 생성)
def mean_of_n(nums):
    result=0
    for num in nums:
        result+=num
    r1=result/len(nums)
    return r1
def max3(nums):
    max_val=int(nums[0])
    for num in nums:
        if max_val<int(num):
            max_val=int(num)
    return max_val
def min3(nums):
    min_val=int(nums[0])
    for num in nums:
        if min_val>int(num):
            min_val=int(num)
    return min_val
nums=list(map(int,input('정수를 여러 개 입력하시오:').split(' ')))
print('평균값은:','{:.1f}',format(mean_of_n(nums)))
print('최댓값은:',max3(nums))
print('최소값은:',min3(nums))
#4.10
x1=int(input('x1 좌표를 입력하시오 :'))
y1=int(input('y1 좌표를 입력하시오 :'))
x2=int(input('x2 좌표를 입력하시오 :'))
y2=int(input('y2 좌표를 입력하시오 :'))
def distance(x1,y1,x2,y2):
    r1=+((x1-x2)**2+(y1-y2)**2)**0.5
    return r1   
print('두점의 거리:',distance(x1,y1,x2,y2))
#4.11
x1=int(input('x1 좌표를 입력하시오 :'))
y1=int(input('y1 좌표를 입력하시오 :'))
x2=int(input('x2 좌표를 입력하시오 :'))
y2=int(input('y2 좌표를 입력하시오 :'))
def area(x1,y1,x2,y2):
    r1=+((x2-x1)*(y2-y1))/2
    return r1   
print('직각감각형의 면적은:',area(x1,y1,x2,y2))
#4.12
width=int(input('밑변을 입력하시오:'))
height=int(input('높이을 입력하시오:'))
def cal_area(width,height):
    area=(width*height)/2
    return area
print('삼각형의 면적:',cal_area(width,height))
#4.13
pi=3.14
#1 모서리 길이가 12인 정육면체의 부피
def square(s):
    print(s**3)
square(12) #1728
#2 모서리 길이가 20인 정육면체의 부피
def square(s):
    print(s**3)
square(20) #8000
#3 가로,세로,길이가 각각 3,5,6인 직육면체의 부피
def rectangle(w,h,l):
    print(w*h*l)
rectangle(3,5,6) #90
#4 반지름과 높이가 각각 20,10인 원뿔의 부피
def circle(r,h):
    print((1/3)*pi*(r**2)*h)
circle(20,10) #4186.666666666666
#5 반지름이 15인 구의 부피
def circle1(r):
    print((4/3)*pi*(r**3))
circle1(15) 
#6 반지름과 높이가 각각 20,10인 원기둥
def circle2(r,h):
   print(3.14*(r**2)*h)
circle2(20,10) #12560.0

#4.14
print('세 수를 입력하세요:')
num1=int(input())
num2=int(input())
num3=int(input())

def sort3(num1,num2,num3):
    alist=[]
    alist.append(num1)
    alist.append(num2)
    alist.append(num3)
    alist=sorted(alist)
    return alist
a=sort3(num1,num2,num3)
print('정렬된 리스트는 다음과 같습니다:',a[0],a[1],a[2])
#4.15
def my_sort(*nums):
    list_ed=[*nums]
    list_ed=sorted(list_ed)
    return list_ed
print(my_sort(45,3,4,56,5))
# 4.16
inputstr=input('쉼표로 구분된 정수를 여러 개 입력하시오 :')
inputlist=inputstr.split(',')
int_list=list(map(int,inputlist))
print('입력된 정수의 리스트 : ',int_list)
int_list.sort()
for a in int_list:
    print(a, end=' ')

    
#4.17
def sum_range(n1,n2):
    return int((n1+n2)*(n2-n1+1)/2)

print(f'10에서 20까지의 정수의 합 : {sum_range(10,20)}') #165
print(f'40에서 100까지의 정수의 합 : {sum_range(40,100)}') #4270
#4.18
def min_pro(a,b):
    c=0
    ex=b-1
    for i in range(min(a,ex),0,-1):
        if a%i==0 and ex%i==0:
            c=a*ex/i
            break
    for i in range(min(c,b),0,-1):
        if c%i==0 and b%i==0:
            print(b*c /i)
            break
a=int(input("범위의 시작 정수 :"))
b=int(input("범위의 마지막 정수 :"))
min_pro(a,b)

#2번째 방법
def least_com(n1,n2):
    cnt=1
    while 1:
        com=0
        for i in range(n1, n2+1):
            if cnt%i==0:
                com +=1
            else:
                continue
            if (n2-n1+1)==com:
                return cnt
n1=int(input('범위의 시작 정수 :'))
n2=int(input('범위의 마지막 정수 :'))
print(f'{n1}에서 {n2}까지의 정수들의 최소 공배수는 : {least_com(n1,n2)}')

#4.19
def fibo(n):
    if n<=1:
        return 1
    else:
        return (fibo(n-1)+fibo(n-2))
n=int(input('fibo(n)의 n을 입력하세요:'))
print(f'fibo({n})',fibo(n))
#4.20
def fibonacci(i):
    if i==0 or i==1:
        return 1
    else:
        return fibonacci(i-1)+fibonacci(i-2)
for k in range(0,16):
    print(f'fibo(  {k})={fibonacci(k)}')
#4.21
person_num=input('주민번호 첫 6숫자 형식 입력')
year=person_num[:2]
month=person_num[2:4]
day=person_num[4:6]
if int(year)>=51:
    year='19'+person_num[:2]
else:
    year='20'+person_num[:2]
print(f'{year}년 {month}월 {day}일')
#2번째 방법
def dateform(datev):
  datel=list(datev)
  if int(datel[0]+datel[1]) >=51:
    year=1900+int(datel[0]+datel[1])
  else:
    year=2000+int(datel[0]+datel[1])
  mon=int(datel[2]+datel[3])
  day=int(datel[4]+datel[5])
  return '{:4d}년 {:2d}월 {:2d}일'.format(year,mon,day)
print(dateform(input('주민등록번호 첫 6 숫자 형식 입력 : ')))
#4.22
import datetime as d
date=d.datetime.now()
print(date)
y,m,d=date.year,date.month,date.day
print(f'현재시간은{y}년{m}월{d}일')
if len(str(m))==1:
    m='0'+str(m)
if len(str(d))==1:
    d='0'+str(d)
print(f'주민번호 앞자리는 {str(y)[2:]}{m}{d}')
# #4.23
def area_and_circumgerence(r):
  l=2*r*3.14
  a=(r**2)*3.14
  return l,a
while(True):
  r=int(input('반지름을 입력하시오 :'))
  if r<0:
    print('프로그램을 종료합니다')
    break
  else:
    l,a=area_and_circumgerence(r)
    print("넓이: %7.3f 둘레: %7.3f"%(a,l))
#4.24
import string #string.punctuation :모든 구두점을 담고 있는 리스트 !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 
n=input()
list=[]
start=0
for i in range(len(n)):
  if n[i] in string.punctuation or n[i]==' ' :
    list.append(n[start:i])
    start=i+1
  if '' in list:
    list.remove('')
list=sorted(list)
print(list)

#2(다른 방법)
in_str=input('여러 단어로 이루어진 글을 입력하세요  :')
s_char=['.',',']
#4.25
s1='kang young min'
s2='kang young-min'
s3='park dong min'
s4='park dong-min'
n=[s1,s2,s3,s4]


for i in n:
    uppern=''
    for word in i:
        if word.isalpha()==True:
           uppern+=word.upper()
    count=0
    for j in uppern:
        if j=='N':
            count+=1
    print(f'{i}은{uppern}으로 수정')
    print(f'{uppern}은 {count}의 N이 나타남')

#4.26
n=list(map(str,input('주어진 문자열:').split(',')))
print(n)
change_count=0
for i in n:
    #리스트목록에 접근
   citiy_name=''
   city_start_num=0
   city_end_num=0
   
   for j in range(len(i)):
        #리스트 목록하나중 문자열에 접근
       if i[j]=='(':
           city_start_num=j+1
       if i[j]==' ':
           city_end_num=j
   if i[city_start_num:city_end_num]=='Bython':
       #문자열 변경불가
       print(i)
       changei=list(i)
       changei[city_start_num]='P'
       newi="".join(changei) #newi=리스트와 된 걸 다시 문자열로
       originindexnum=n.index(i)
        #문자열 통채로 인덱스를 찾아냄
       n[originindexnum]=newi
       n1="".join(n) #n 리스트 전체를 문자열로 바꿔준다
       change_count+=1     
print(f'수정된 문자열  :{n1} ')
print(f' Bython 문자열은 모두 {change_count}번 수정했습니다')
#4.27
num=float(input('1보다 작고 0보다 큰 소수를 입력하세요: '))
def unit_fraction(frac):
    i=1
    while(True):
        단위분수1=1/i
        단위분수2=1/(i+1)
        if 단위분수1>frac and 단위분수2<frac:
            if(단위분수1-frac<frac-단위분수2):
                print(f'가장 가까운 단위분수는1/{i}이며 이 값은{단위분수1}입니다')
                return
            else:
                print(f'가장 가까운 단위분수는1/{i+1}이며 이 값은{단위분수2}입니다')
                return
        else:
            i+=1
unit_fraction(num)
#다른 코드
def unit_fraction(frace):
    com1=com2=0
    cnt=2
    if frace >=0.5:
        return cnt
    while 1:
        if frace >=(1/(cnt+1)):
            com1=abs(frace- (1/cnt))
            com2=abs(frace-(1/(cnt+1)))
            if com1>com2:
                return cnt +1
            else:
                return cnt
        cnt +=1
frace=float(input('1보다 작고 0보다 큰 소수를 입력하세요 :'))
N=unit_fraction(frace)
print(f'가장 가까운 단위분수는 1/{N}이며, 이 값은 {1/N}입니다')



#4.28
#1
def factorial(k): 
    if k<=1:             
        return 1
    else:
        return k*factorial(k-1) 
k=5
print(factorial(5))
# #2
def euler(n):
    d=0
    for i in range(n+1):
        d+=1/factorial(i)
    return d
print('{:.5f}'.format(euler(5)))
print('{:.5f}'.format(euler(20)))
