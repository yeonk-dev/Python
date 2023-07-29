#5.1 리스트 자료형의 필요성
#실습: 여러 개의 변수를 생성하고 사용하기
# s0=87
# s1=84
# s2=95
# s3=67
# print(s0,s3) #87 67
# #실습: 수치 값을 가진 리스트 만들기
# s_list=[87,84,95,67,88,94,63]
# print(s_list) #[87, 84, 95, 67, 88, 94, 63]
# print(s_list[0],s_list[3]) #87 67
# #실습: 문자열과 복합 자료값을 가진 리스트 만들기
# fruits=['banana','apple','orrange']
# print(fruits) #['banana', 'apple', 'orrange']
# mixed_list=[100,200,'yeah',400] 
# print(mixed_list) #[100, 200, 'yeah', 400]
# #실습: 다양한 방법으로 리스트 만들기
# list1=list()
# lis2=[]
# list3=list((1,2,3)) #튜플로 리스트 생성
# print(list3) #[1, 2, 3]
# list4=list(range(1,10)) #range() 함수로 부터 리스트 생성
# print(list4) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
# list5=list('abceef') #문자열로 부터 리스트 생성
# print(list5) #['a', 'b', 'c', 'e', 'e', 'f']

# #lab 5-1: 리스트의 생성
# #1
# even_list=list(range(2,11,2))
# print(even_list) #[2, 4, 6, 8, 10]
# nations=list(('korea','china','india','nepal'))
# print(nations) #['korea', 'china', 'india', 'nepal']
# friends=list(('길동','철수','은지','지은','영민'))
# print(friends) #['길동', '철수', '은지', '지은', '영민']
# string=list('XYZ')
# print(string) #['X', 'Y', 'Z']

# #5.2 리스트의 인덱스
# #실습: 6개의 원소를 가지는 리스트 만들기
# n_list=[11,22,33,44,55,66]
# print(n_list) #[11, 22, 33, 44, 55, 66]
# print(len(n_list)) #6
# print(n_list[0]) #11
# #실습: 리스트 인덱스를 통한 요소의 접근
# n_list=[11,22,33,44,55,66]
# print(n_list[5]) #66
# # print(n_list[6]) #IndexError: list index out of range :리스트의 일곱 번째 요소값은 존재하지 않음
# #실습 : 리스트의 음수 인덱스 사용법
# n_list=[11,22,33,44,55,66]
# print(n_list[-1]) #66 리스트의 마지막 요소 값
# print(n_list[-2]) #55
# #lab 5-2 : 리스트의 생성과 인덱싱
# prime_list=[2,3,5,7]
# print('prim_list의 첫 원소:',prime_list[0]) #prim_list의 첫 원소: 2
# print('prim_list의 마지막 원소:',prime_list[3]) #prim_list의 마지막 원소: 7
# print('prim_list의 마지막 원소:',prime_list[-1]) #prim_list의 마지막 원소: 7
# nations=list(('korea','china','russia','mongol'))
# print('nations의 첫 원소:',nations[0]) #nations의 첫 원소: korea
# print('nations의 마지막 원소:',nations[-1]) #nations의 마지막 원소: mongol
# print('nations의 마지막 원소:',nations[len(nations)-1]) #nations의 마지막 원소: mongol

#5.3 리스트 항목의 추가와 삭제
#실습: 리스트의 append() 메소드를 사용한 항목의 추가
a_list=['a','b','c','d','e']
a_list.append('f')
print(a_list) #['a', 'b', 'c', 'd', 'e', 'f']
n_list=[10,20]
n_list.append(30)
print(n_list) #[10, 20, 30]
#코드 5-1: del 명령어를 이용한 리스트의 항복 삭제
n_list=[11,22,33,44,55,66]
print(n_list) #[11, 22, 33, 44, 55, 66]
del n_list[3]
print(n_list) #[11, 22, 33, 55, 66]
#코드 5-2: remove() 메소드를 사용한 리스트의 항목 삭제
n_list=[11,22,33,44,55,66]
print(n_list)
n_list.remove(44)
print(n_list) #[11, 22, 33, 55, 66]
#코드 5-3: 리스트 내부에 존재하지 않는 항목을 삭제하는 경우
n_list=[11,22,33,44,55,66]
print(n_list)
# n_list.remove(77) #ValueError: list.remove(x): x not in list :77이 리스트 내부에 있지 않음
# print(n_list)