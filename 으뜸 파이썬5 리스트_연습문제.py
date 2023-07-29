#5.1
list_ex=[10,20,30,40,50,60,70]
high=5
low=3
print(list_ex[low]) #40
print(list_ex[low+2]) #60
print(list_ex[high-low]) #30
print(list_ex[low-high]) #60
print(list_ex[-1]) #70
print(list_ex[-low]) #50
print(list_ex[2*3]) #70
print(list_ex[2]*3) #90
print(list_ex[5%4]) #20
print(len(list_ex)) #7
#5.2
spell=['s','w','e','e','t']
print(spell) #['s', 'w', 'e', 'e', 't']
spell[3]='a'
print(spell) #['s', 'w', 'e', 'a', 't']
spell[4]='r'
print(spell) #['s', 'w', 'e', 'a', 'r']
print(spell*2) #['s', 'w', 'e', 'a', 'r', 's', 'w', 'e', 'a', 'r']
#5.3
list1=[3,5,7]
list2=[2,3,4,5,6]
for i in list1:
    for j in list2:
        print(f'{i}*{j}={i*j}')
#5.4
a=[2,3,4,5,6]
rev_a=(a.pop(4),a.pop(3),a.pop(2),a.pop(1),(a.pop(0)))
print(list(rev_a)) #[6, 5, 4, 3, 2]
#5.5
list1=['I like','I love']
list2=['pancakes','kiwi juice','espresso']
for i in list2:
    if ('I like' in list1):
        print('I like '+ i)
for i in list2:
    if ('I love' in list1):
        print('I love '+i)
#5.6
list1=[2,3,4,1,32]
print(max(list1)) #32
print(sum(list1)) #42
list1.remove(32)
print(list1) #[2, 3, 4, 1]
list1.reverse()
print(list1) #[1, 4, 3, 2]
list1.sort()
print(list1) #[1, 2, 3, 4]
#5.7
n_list=[10,20,30,50,60]
s=0
for i in n_list:
    s+=i
print('리스트의 원소들 :', n_list) #리스트의 원소들 : [10, 20, 30, 50, 60]
print('리스트 원소들의 합 :',s) #리스트 원소들의 합 : 170
#5.8
n_list=[10,20,30,50,60]
s=1
for i in n_list:
    s*=i
print('리스트 원소들 : ',n_list) #리스트 원소들 :  [10, 20, 30, 50, 60]
print('리스트 원소들의 곱 :',s) #리스트 원소들의 곱 : 18000000
#5.9
n_list=[10,20,30,50,60]
n_list.sort(reverse=True)
print('리스트 원소들 : ',n_list) #리스트 원소들 :  [10, 20, 30, 50, 60]
print('리스트 원소들 중 최댓값 :',n_list[0]) #리스트 원소들 중 최댓값 : 60
# #5.10
n_list=[10,20,30,50,60]
n_list.sort()
print('리스트 원소들 : ',n_list) #리스트 원소들 :  [10, 20, 30, 50, 60]
print('리스트 원소들 중 최소값 :',n_list[0]) #리스트 원소들 중 최소값 : 10
#5.11
n_list=list(map(int,input('5개의 수를 입력하세요: ').split()))
print('합 :',sum(n_list))
print('평균 :',sum(n_list)/len(n_list))
print('최댓값 :',max(n_list))
print('최솟값 :',min(n_list))

#5.12
n=int(input('n을 입력하세요 :'))
n_list=list(map(int,input(f'{n}개의 수를 입력하세요: ').split()))
print('합 :',sum(n_list))
print('평균 :',sum(n_list)/len(n_list))
print('최댓값 :',max(n_list))
print('최솟값 :',min(n_list))      

#5.13
num=list(map(int,input('10개의 수를 입력하세요:').split()))
print('합 :',sum(num))
print('평균 :',sum(num)/len(num))
b=sum(num)
c=b/len(num)
d=0
for i in range(0,10,1):
    d+=((num[i]-c)**2)/len(num)
print('표준 편차 :',round(d**0.5,2))
#5.14
spell=['h','a','p','p','y',' ','b','i','r','t','h','d','a','y']
print(spell[1:5]) #['a', 'p', 'p', 'y']
print(spell[:]) #['h', 'a', 'p', 'p', 'y', ' ', 'b', 'i', 'r', 't', 'h', 'd', 'a', 'y']
print(spell[:5]) #['h', 'a', 'p', 'p', 'y']
print(spell[6:]) #['b', 'i', 'r', 't', 'h', 'd', 'a', 'y']
print(spell[:2]+spell[9:]) #['h', 'a', 't', 'h', 'd', 'a', 'y']
#5.15
greet='Have a beautiful day.'
print(greet[0:5]) #Have
print(greet[7:16]) #beautiful
print(greet[17:20]) #day
#5.16
s="Birthday"
print(s[:5]) #Birth
print(s[5:]) #day
print(s[1:-1]) #irthda
print(s[::-1]) #yadhtriB
print('day' in s) #True
print('birth' in s) #False
print('Birth' in s) #True
print('Birth' not in s) #False
#5.17
#1
animals=['dog','cat','tiger','lion']
print(animals) #['dog', 'cat', 'tiger', 'lion']
#2
animals=['dog','cat','tiger','lion']
del animals[0]
animals=animals+['dog'] #animals.insert(3,'dog')
print(animals)
#3
animals=['dog','cat','tiger','lion']
for animal in animals:
    print('I love',animal)
#5.18
#1
strs = ["abc", "bcd", "bcdefg", "abba","cddc",'opq']

min_str = strs[0]
for i in range(1, len(strs)):
     if len(min_str) > len(strs[i]):
       min_str = strs[i]
print("가장 길이가 짧은 문자열 :",min_str) #가장 길이가 짧은 문자열 : abc
#2
strs = ["abc", "bcd", "bcdefg", "abba","cddc",'opq']

max_str = strs[0]
for i in range(1, len(strs)):
     if len(max_str) < len(strs[i]):
       max_str = strs[i]
print("가장 길이가 긴 문자열 :",max_str)
#3
strs = ["abc", "bcd", "bcdefg", "abba","cddc",'opq']
strs=sorted(strs, key=len)
short_len=len(strs[0])
print('길이가 가장짧은 문자열:',end=' ')
for i in strs:
  if len(i)==short_len:
    print(f'\'{i}\'',end=' ')
#5.19
s_list=['abc','bcd','abc','abba','cddc','opq','opq']
new_s_list=[]
for i in s_list:
    if i in new_s_list:
        continue
    else:
        new_s_list.append(i)
print('s_list =',s_list)
print('new_s_list =',new_s_list)
#빠른버전
new_s_list=list(set(s_list))
print(new_s_list)

#5.20
src1='aaaabcccaaaaaccccfg'


def 문자압축(src):
    i=0
    output=''
    while(i!=len(src)):
        start=src[i]
        output+=str(start)
        j=i+1
        count=1
        if j==len(src):
            output+=str(count)
            break
        while(True):
            if src[j]!=start:
                i=j
                output+=str(count)
                break
            else:
                count+=1
                j+=1  
    return output 
    
print(문자압축(src1))

#5.21
def 압축해제(src):
    output=''
    for i in range(0,len(src),2):
        alpha=src[i]
        repeat=int(src[i+1])
        for j in range(repeat):
            output+=alpha
    return output
src2='a2b3c6a2c3f1g1'
print(압축해제(src2))
#5.22
n=int(input())
l1=[]
for i in range(i,n*n+1):
    l1.append(i)
for j in range(0,n*n,5):
    if j%2==0:
        l2=l1[j:j+5]
        for i in l2:
            print(f'{i}]\t',end='')
        print()
    else:
        l2=l1[j+4:j-1:-1]
        for i in l2:
            print(f'{i}\t',end='')
        print()
#5.23
# 이름 나이 성별(1 남자 0여자) 키 몸무게
p1=['온달',20,1,180.0,100.0]
p2=['이사부',25,1,170.0,70.0]
p3=['평강',22,0,169.0,60.0]
p4=['혁거세',40,1,150.0,50.0]

plists=p1+p2+p3+p4
print(plists)
#1
def how_many_p(plist):
    many=len(plist)//5
    return many
npersons=how_many_p(plists)
print(str(npersons))
#2
def compute_average_age(plist):
    person_num=how_many_p(plist)
    average_age=0
    for i in range(1,len(plist),5):
        average_age+=plist[i]
    average_age=average_age/person_num
    return average_age
average_age=compute_average_age(plists)
print(f'평균나이는{average_age}세 입니다')
        
#3

def count_man_women(plist):
    man=0
    women=0
    for i in range(2,len(plist),5):
        if plist[i]==0:
            women+=1
        else:
            man+=1
    return man,women
m_num,w_num=count_man_women(plists)
print(f'리스트에는 남자가{m_num} 명 여자가{w_num}명입니다')


#4
def display_person(plist):
    for i in range(0,len(plist),5):
        print(list(plist[i:i+5]))
display_person(plists)

#5.24
def 진약수구하기():
    for i in range(1,10000+1):
        약수모음=[]
        #약수 리스트에 넣는 알고리즘
        for j in range(1,i):
            if i%j==0:
                약수모음.append(j)
        if sum(약수모음)==i:
            sums=sum(약수모음)
            print(f'{i}는 완전수입니다.')
            print(f'{i}의 약수:{약수모음},약수의 합{sums}')
            
진약수구하기()