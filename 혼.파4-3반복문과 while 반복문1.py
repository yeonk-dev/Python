#범위 range
#매개변수에 숫자 한 개 넣기
a=range(5)
print(a)   #range(0,5)
print(list(range(10)))  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#매개변수에 숫자 두 개 넣기
print(list(range(0,5)))    #[0, 1, 2, 3, 4]   #list(range(a,b)) a부터 b-1 까지 정수로 범위 출력
#매개변수에 숫자 세 개 넣기
print(list(range(0,10,2)))  #range(a,b,c)  a부터 c씩 증가하면서 b-1까지의 정수로 범위 출력
print(list(range(1,14,3)))  #[1, 4, 7, 10, 13]
#강조
a=range(0,10+1)   #10을 반드시 포함해야한다는 것을 강조하고 싶을 때 수식 사용
print(list(a))    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#range() 함수의 매개변수로는 반드시 정수(integer) 입력
n=10
b=range(0,int(n/2))  #실수를 정수로 바꾸기 사용
print(list(b))     #[0, 1, 2, 3, 4]
c=range(0,n//2)    #정수 나누기 연산자 사용
print(list(c))     #[0, 1, 2, 3, 4]
