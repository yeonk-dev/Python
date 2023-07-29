#6.5 리스트와 딕셔너리의 비교
#코드6-1: 리스트의 항목 삭제와 lst[1] 항목의 변화 여부
# lst=[11,22,33,44,55]
# print('pop(0) 이전 :',lst) #pop(0) 이전 : [11, 22, 33, 44, 55]
# print('pop(0) 이전 lst[1] :',lst[1]) #pop(0) 이전 lst[1] : 22
# lst.pop(0)
# print('pop(0) 이후:',lst) #pop(0) 이후: [22, 33, 44, 55]
# print('pop(0) 이후 lst[1]:',lst[1]) #pop(0) 이후 lst[1]: 33
# #코드 6-2: 딕셔너리 항목 삭제와 dic[1] 항목의 변화 여부
# dic={0:11,1:22,2:33,3:44,4:55}
# #딕셔너리의 (키,값) 튜플쌍을 반환하는 items() 함수로 항목 출력
# print('pop(0) 이전 :',dic.items()) #pop(0) 이전 : dict_items([(0, 11), (1, 22), (2, 33), (3, 44), (4, 55)])
# print('pop(0) 이전 dic[1]=',dic[1]) #pop(0) 이전 dic[1]= 2
# dic.pop(0)
# print('pop(0) 이후 ',dic.items()) #pop(0) 이후  dict_items([(1, 22), (2, 33), (3, 44), (4, 55)])
# print('pop(0) 이후 dic[1]=',dic[1]) #pop(0) 이후 dic[1]= 22
#lab 6-5 :딕셔너리의 활용
fruits_dic={'apple':6000,'melon':3000,'banana':5000,'orange':7000}
print(list(fruits_dic.keys()))#['apple', 'melon', 'banana', 'orange']
print(list(fruits_dic.values())) #[6000, 3000, 5000, 7000]
print('fruits_dic 딕셔너리의 항목의 개수 :',len(fruits_dic)) #fruits_dic 딕셔너리의 항목의 개수 : 4
print('apple'  in fruits_dic) #True
print('mango'  in fruits_dic) #False

#6.6 튜플 자료형
#실습 : 튜플의 생성과 조회
t=(1,2,3,4)
print(t[0]) #1
#하나의 요소를 가지는 튜플 선언
tup=(100)
print(type(tup)) #<class 'int'> 
#올바른 선언
tup=(100,)
print(type(tup)) #<class 'tuple'>
#실습 : 튜플 항목에 대한 할당 연산은 오류를 발생시킴
#t=(0,1,2,3,4)
#t[0]=100
#print(t) #TypeError: 'tuple' object does not support item assignment
#패킹과 언패킹
a=(1,2)# 튜플 패킹
print(a[0]) #1 - 튜플 항목에 대한 참조
c=(3,4)
d,e=c
print(d) #3 #튜플 패킹
print(e) #4 #튜플 언 패킹
#코드 6-3: 임시변수 temp를 이용한 값의 교환
a=100
b=200
print('swap 이전: a=',a,'b =',b) #swap 이전: a= 100 b = 200
temp=a
a=b
b=temp
print('swap 이후 : a =',a,'b =',b) #swap 이후 : a = 200 b = 100
#코드 6-4: 튜플과 할당 연산자를 이용한 간단한 swap
a=100
b=200
print('swap 이전 : a=',a,'b=',b) #swap 이전 : a= 100 b= 200
a,b=b,a
print('swap 이후 : a=',a,'b=',b) #swap 이후 : a= 200 b= 100
#lab 6-6 : 튜플의 생성과 패킹 ,언패킹
the_day=(1919,3,1)
year,month,day=the_day
print(f'{year}년 {month}월 {day}일은 삼일절 입니다.') #1919년 3월 1일은 삼일절 입니다.
lst=[10,20,30]
lst=tuple(lst)
c,b,a=lst
print('a=',a) #a= 30
print('b=',b) #b= 20
print('c=',c) #c= 10

#6.7 튜플의 연산
#실습 : 튜플의 +와 *연산
t0=(10,20,30)
t1=t0+t0
print(t1) #(10, 20, 30, 10, 20, 30)
t2=t0*2
print(t2) #(10, 20, 30, 10, 20, 30)
# t3=t0+40  튜플과 정수는 덧셈 연산을 할 수 없음
# print(t3)    TypeError: can only concatenate tuple (not "int") to tuple
t4=t0+(40,)
print(t4) #(10, 20, 30, 40)
#튜플 메소드
#count(x) 튜플내에 특정 값 X가 몇 개 있는가를 알려줌
#index(x) 튜플내에 특정 값 X의 위치를 알려줌
t=(10,20,30,20,20,10,50)
print(t.count(20)) #3 - 튜플에 포함된 10 원소의 개수
print(t.index(30)) #2 -튜플에 포함된 30 원소의 인덱스
#코드 6-5 : 튜플의 항목 값을 리스트로 이용하여 변경
t_fruits=('apple','orange','water melon')
print('변경 전 :',t_fruits) #변경 전 : ('apple', 'orange', 'water melon')
f_list=list(t_fruits) #튜플을 리스트로 반환
print(f_list) #['apple', 'orange', 'water melon']
f_list[1]='kiwi'
t_fruits=tuple(f_list)
print('변경 후 :',t_fruits) #변경 후 : ('apple', 'kiwi', 'water melon')
#lab 6-7 :튜플의 활용
person=('홍길동', 2019001, 179)
# person[1]=2019003
# print(person)  -TypeError: 'tuple' object does not support item assignment
person=list(person)
person[1]=2019003
person=tuple(person)
print('학번 변동 후:',person)