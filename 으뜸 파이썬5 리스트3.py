#5.7 리스트와 연산
#코드 5-6: 두 리스트를 합치는 연산자
# list1=[11,22,33,44]
# list2=[55,66]
# print(list1) #[11, 22, 33, 44]
# print(list1+list2) #[11, 22, 33, 44, 55, 66]
# #코드 5-7: 두 리스트 합치는 연산자 +를 이용하여 그 결과를 저장함
# list1=[11,22,33,44]
# list2=[55,66]
# list3=list1+list2
# print(list3) #[11, 22, 33, 44, 55, 66]
# #실습: * 연산자를 이용한 반복 리스트
# list1=[1,2,3,4]
# print(list1*2) #[1, 2, 3, 4, 1, 2, 3, 4]
# list2=list1*3
# print(list2) #[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# #실습: 문법오류를 유발하는 두 리스트의 * 연산
# list1=[1,2,3,4]
# list2=[10,20,30]
# list2=list1*3
# print(list2) #[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
#실습 : 문법오류를 유발하는 두 리스트의 * 연산
# list1=[1,2,3,4]
# list2=[10,20,30]
# print(list1*list2) #TypeError: can't multiply sequence by non-int of type 'list'
#실습: ==연산자를 이용한 리스트의 비교
# list1=[1,2,3,4]
# list2=[1,2,3,4]
# print(list1==list2) #True
# list3=[4,1,2,3]
# print(list1==list3) #False
#실습 : >, < 연산자를 이용한 리스트의 비교
# list1=[1,2,3,4]
# list2=[2,3,3,4]
# print(list1> list2) #False
# print(list1< list2) #True
#lab 5-6: 리스트 연산
# n_list=[1,2,3]
# n=int(input('반복할 정수를 입력하시오 :'))
# print(n_list*n) #[1, 2, 3, 1, 2, 3, 1, 2, 3]

#5.8 리스트의 내용 갱신을 위한 방법
#코드 5-8: 리스트 요소들을 하나하나 방문하며 10을 곱하는 기능
list1=[10,20,30,40,50]
i=0
for n in list1:
    list1[i]=n*10
    i=i+1
print(list1) #[100, 200, 300, 400, 500]
#코드 5-9: 리스트의 축약 표현을 사용하여 10을 곱하는 기능
list1=[10,20,30,40,50]
list1=[n*10 for n in list1]
print(list1) #[100, 200, 300, 400, 500]
#코드 5-10: 람다 함수와 map을 이용하여 리스트 요소들을 조직하기
list1=[10,20,30,40,50]
list1=list(map(lambda x: x*10, list1))
print(list1) #[100, 200, 300, 400, 500]
#5.9 리스트의 슬라이싱
#실습 : 리스트와 슬라이싱
a_list=[10,20,30,40,50,60,70,80]
print(a_list[1:5]) #[20, 30, 40, 50]
print(a_list[0:1]) #[10]
print(a_list[0:2]) #[10, 20]
print(a_list[0:5]) #[10, 20, 30, 40, 50]
print(a_list[1:])  #[20, 30, 40, 50, 60, 70, 80]
print(a_list[:5])  #[10, 20, 30, 40, 50]
print(a_list[:])   #[10, 20, 30, 40, 50, 60, 70, 80]
print(a_list[-7:-2]) #[20, 30, 40, 50, 60]
print(a_list[-7:]) #[20, 30, 40, 50, 60, 70, 80]
print(a_list[:-2]) #[10, 20, 30, 40, 50, 60]
print(a_list[-2:]) #[70, 80]
print(a_list[:-2]+a_list[-2:]) #[10, 20, 30, 40, 50, 60, 70, 80]
print(a_list[-2:]+a_list[:-2]) #[70, 80, 10, 20, 30, 40, 50, 60]
print(a_list[0:8:3]) #[10, 40, 70]
print(a_list[::-1]) #[80, 70, 60, 50, 40, 30, 20, 10]

#lab 5-7: 리스트의 슬라이싱
#1
n_list=list(range(15))
print(n_list) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#2
s_list1=n_list[0:5]
print(s_list1) #[0, 1, 2, 3, 4]
s_list2=n_list[5:11]
print(s_list2) #[5, 6, 7, 8, 9, 10]
s_list3=n_list[11:15]
print(s_list3) #[11, 12, 13, 14]
s_list4=n_list[2:11:2]
print(s_list4) #[2, 4, 6, 8, 10]
s_list5=n_list[10:5:-1]
print(s_list5) #[10, 9, 8, 7, 6]
s_list6=n_list[10:1:-2]
print(s_list6) #[10, 8, 6, 4, 2]