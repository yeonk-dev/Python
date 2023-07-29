#튜플(tuple):함수와 함께 많이 사용되는 리스트와 비슷한 자료형,리스트와 다르게 한번 결정된 요소는 바꿀 수 없음
#람다(lambda):매개변수로 함수를 전달하기 위해 함수구분을 작성하는 것이 번거롭거나
#             코드 공간 낭비라 생각이 들때 함수를 간단하고 쉽게 선언하는 방법
#튜플(tuple) :(데이터, 데이터, 데이터 ...)
tuple_list=(10,20,30)
print(tuple_list[0]) #
#tuple_test[1]=30  / NameError: name 'tuple_test' is not defined 내부 요소 변경 불가능
#요소를 하나만 가지는 리스트 [273]
#요소를 하나만 가지는 튜플 (273, )

#괄호없는 튜플
#1.리스트와 튜플의 특이한 사용
[a,b]=[10,20]
(c,d)=(10,20)
print("a=",a) #a=10
print("c=",c) #c=10  :리스트/튜플 모두 변수를 선언하고 할당가능
#2.괄호가 없는 튜플
tuple_test=10,20,30,40
print("괄호가 없는 튜플의 값과 자료형 출력") #괄호가 없는 튜플의 값과 자료형 출력
print("tuple_test:",tuple_test)           #tuple_test: (10, 20, 30, 40)
print("type(tuple_test):",type(tuple_test)) #type(tuple_test): <class 'tuple'>
a,b,c=10,20,30
print("괄호가 없는 튜플을 활용한 할당")  #괄호가 없는 튜플을 활용한 할당
print("a=",a)                          #a=10
print("b=",b)                          #b=20
print("c=",c)                          #c=30
#3.변수의 값을 교환하는 튜플
a,b=10,20
print("교환 전 값")
print("a=",a) #a=10
print("b=",b) #b=20
a,b=b,a    #값을 교환
print("교환 후 값")
print("a=",a) #a=20
print("b=",b) #b=10


