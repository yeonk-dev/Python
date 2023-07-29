#5.4 멤버 연산자 : in, not in
#실습: 멤버 연산자 in과 리스트
a_list=[10,20,30,40]
print(10 in a_list) #True
print(10 not in a_list) #False
#코드 5-4: 리스트 내부에 값이 존재하는가를 확인하는 기능
n_list=[11,22,33,44,55,66]
print(88 in n_list) #False
print(55 in n_list) #True
#코드 5-5: in 연산자를 이용한 안전한 원소 삭제
n_list=[11,22,33,44,55,66]
if (55 in n_list):
    n_list.remove(55)
if (88 in n_list):
    n_list.remove(88)
print(n_list) #[11, 22, 33, 44, 66]
#lab 5-3: 리스트의 삽입과 삭제,in 연산자
#1
prime_list=[2,3,5,7]
print('소수 목록 :',prime_list)
prime_list.append(11)
print('추가 후 소수 목록:',prime_list) #추가 후 소수 목록: [2, 3, 5, 7, 11]
#2
print('삭제 전 소수 목록:',prime_list)
prime_list.remove(3)
print('삭제 후 소수 목록:',prime_list) #삭제 후 소수 목록: [2, 5, 7, 11]
#3
nation=['korea','china','russia','malaysia']
print('국가 목록:',nation) #국가 목록: ['korea', 'china', 'russia', 'malaysia']
nation.append('nepal')
print('추가 후 국가 목록:',nation) #추가 후 국가 목록: ['korea', 'china', 'russia', 'malaysia', 'nepal']
#4
if ('japan'in nation):
    print('japan 는 국가 목록에 있습니다.')
else:
    print('japan 는 국가 목록에 없습니다.')
if ('russia' in nation):
    print('russia 는 국가 목록에 있습니다.')
else:
    print('russia 는 국가 목록에 없습니다.')
#5.5 리스트에 적용되는 내장함수
#실습: 리스트와 내장함수 min(), max(), sum()
list1=[20,10,40,50,30]
print(min(list1)) #10
print(max(list1)) #50
print(sum(list1)) #150
#실습 : 문자열 리스트와 내장함수 min(), max()
fruits=['banana','orange','apple']
print(min(fruits)) #영어사전 순서로 가장 앞에 있는 단어 반환 #apple
print(max(fruits)) #영어사전 순서로 가장 뒤에 있는 단어를 반환 #orange
#실습 : 한글 문자열 리스트와 내장함수 min(), max()
k_fruits=['사과','오렌지','포도','바나나']
print(min(k_fruits)) #영어사전 순서로 가장 앞에 있는 단어 반환  # 바나나
print(max(k_fruits)) #영어사전 순서로 가장 뒤에 있는 단어를 반환 # 포도
#lab 5-4: 리스트의 min()과 max(), len() 함수
#1
prime_list=[2,3,5,7]
avg=sum(prime_list)/len(prime_list)
print('최솟값 :',min(prime_list)) #최솟값 : 2
print('최댓값 :',max(prime_list)) #최댓값 : 7
print('합계 :',sum(prime_list))   #합계 : 17
print('평균 :',avg)               #평균 : 4.25
#2
nation=['korea','china','russia','malaysia']
print('사전에 가장 먼저 나오는 나라 :',min(nation)) #사전에 가장 먼저 나오는 나라 : china
print('사전에 가장 먼저 나오는 나라 :',max(nation)) #사전에 가장 먼저 나오는 나라 : russia

#5.6 리스트의 메소드
#실습: 리스트와 sort() 메소드
list1=[20,10,40,50,30]
list1.sort()
print(list1) #[10, 20, 30, 40, 50]
list1.sort(reverse=True)
print(list1) #[50, 40, 30, 20, 10]
#실습: 원소의 인덱스를 반환하는 index() 메소드
a_list=['a','b','c','d','e']
print(a_list.index('a')) #0
print(a_list.index('b')) #1
# print(a_list.index('x')) #ValueError: 'x' is not in list -오류 발생
#실습 : 리스트의 count() 메소드
b_list=['a','b','c','a','b','a']
print(b_list.count('a')) #3
print(b_list.count('b')) #2
#실습: 리스트의 extend() 메소드
list1=['a','b','c']
list2=[1,2,3]
list1.extend(list2)
print(list1) #['a', 'b', 'c', 1, 2, 3]
list1.extend('d')
print(list1) #['a', 'b', 'c', 1, 2, 3, 'd']
#실습 : 리스트의 insert() 메소드
list1=['a','c','d']
list1.insert(1,'b')
print(list1) #['a', 'b', 'c', 'd']
#실습: 리스트의 remove() 메소드
list1=['a','b','c','b','d']
list1.remove('b') #제일 먼저 나타나는 'b' 원소를 삭제함
print(list1) #['a', 'c', 'b', 'd']
list1.remove('b') #list1에 있는 'b' 원소를 삭제함
print(list1) #['a', 'c', 'd']
#실습 : 리스트의 pop() 메소드
list1=['a','b','c','d']
print(list1.pop()) #d
print(list1) #['a', 'b', 'c']
list1=['a','b','c','d']
print(list1.pop(1))#b
print(list1) #['a', 'c', 'd']
#실습: 리스트의 remove()와 인덱스를 이용한 마지막 원소의 삭제
list1=['a','b','c','d']
list1.remove(list1[-1]) #pop()과 유사하게 리스트의 마지막 원소 삭제
print(list1) #['a', 'b', 'c']
#실습: 리스트의 reverse() 메소드
list1=[10,20,30,40]
list1.reverse() #리스트의 원소를 역순으로 다시 배열함
print(list1) #[40, 30, 20, 10]

#lab 5-5: 리스트 메소드의 응용
#1
a=[1,2,3]
b=[10,20,30]
a.append(b)
print(a) #[1, 2, 3, [10, 20, 30]]
a=[1,2,3]
b=[10,20,30]
a.extend(b)
print(a) #[1, 2, 3, 10, 20, 30]
#2
nlist=list(range(1,11))
print(nlist) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#3
nlist.insert(0,0)
print(nlist) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#4
nlist.reverse()
print(nlist) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#5
print('마지막 원소 =',nlist.pop()) #마지막 원소 = 0
print('nlist =',nlist) #nlist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]








