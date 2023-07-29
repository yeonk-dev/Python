#코드 3-21 : range() 함수를 이용한 for 문의 제어
# for i in range(5):
#     print(i) #0부터 4까지 한줄씩 출력
# #코드 3-22 : for 문의 제어와 print() 함수의 end 키워드 인자 사용방법
# for i in range(5):
#     print(i, end=' ')
# for i in range(0,5):
#     print(i, end=' ') #0 1 2 3 4 0 1 2 3 4
# #코드 3-23 : for 문의 제어와 print() 함수의 end 인자 사용방법
# for i in range(5):
#     print(i, end=' ')
# print() #0 1 2 3 4
# for i in range(0,5):
#     print(i, end= ' ')
# print() #0 1 2 3 4
# #코드 3-24 : range() 함수를 이용한 for 문의 제어와 간격값 사용법
# for i in range(2,5): #표현식1
#     print(i, end=' ') # 2 3 4 '2에서 5-1까지 연속값 2, 3, 3 출력
# print()
# for i in range(0,10,2): #표현식2 : 간격 값을 이용하여 0,2,4,6,8 출력
#     print(i,end=' ') #0 2 4 6 8  
# print()
# for i in range(-2,-10,-2): #표현식3 : 음수 간격 값 사용
#     print(i,end=' ') #-2 -4 -6 -8
# print()
# #반복문의 활용
# #코드 3-25: 연속적인 값의 생성과 누적 덧셈
# s=0
# for i in range(1,11):  #sum() 내장함수와 중복사용시 오류 발생 가능성 있음, 다른 이름 사용
#     s=s+i
# print('1에서 10까지의 합:', s) #1에서 10까지의 합: 55
# #코드 3-26: 누적 덧셈의 중간 결과 출력하기
# s=0
# for i in range(1,11):
#     s=s+i
#     print('i = {}, s = {}'.format(i,s))
# #코드 3-27: 사용자로부터 입력을 받은 후 누적 합계 값 구하기
# n=int(input('합계를 구할 수를 입력하세요 : '))
# s=0
# for i in range(0,n):
#     s=s+(i+1)
# print(f'1부터 {n}까지의 합은 {s}')
# #코드 3-28: 사용자로부터 입력을 받은 후 누적 합계 값 구하기
# n=int(input('합계를 구할 수를 입력하세요 : '))
# s=0
# for i in range(0,n+1):
#     s=s+i
# print(f'1부터 {n}까지의 합은 {s}')

# #팩토리얼 구하기(factorial)
#코드 3-29: for 반복문을 이용한 5 팩토리얼(5!) 계산
# n=int(input('수를 입력하세요 : '))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(f'{n}!={fact}')
#for 문과 리스트
#코드 3-30 : for 문을 이용한 리스트의 정수 객체 순회
# numbers=[11,22,33,44,55,66]
# for n in numbers:
#     print(n, end=' ') #11 22 33 44 55 66 
# #코드 3-31: for 문을 이용한 리스트의 실수 객체 순회
# f_numbers=[1.1,2.5,3.7,5.6,9.2,11.3,6.8]
# for f in f_numbers:
#     print(f, end=' ') #1.1 2.5 3.7 5.6 9.2 11.3 6.8
# #코드 3-32: for 문을 이용한 리스트의 문자열 객체 순회
# s_fruits=['수박','참외','체리','포도']
# for fruit in s_fruits:
#     print(fruit, end=' ') #수박 참외 체리 포도
#코드 3-33: 리스트 항목내 정수 값들의 누적 덧셈
# numbers=[10,20,30,40,50]
# s=0
# for n in numbers:
#     s=s+n
# print('리스트 항목 값의 합 : ',s) #리스트 항목 값의 합 :  150
# #코드 3-34 : sum()함수의 사용
# numbers= [10, 20, 30, 40, 50]
# print('리스트 항목 값의 합 :',sum(numbers))
# #대화창 실습: 대화형 모드를 통한 1-100까지의 합(반복가능 객체)
# print('1에서 100까지의 합 :',sum(range(1,101))) #1에서 100까지의 합 : 5050
# #대화창 실습 : 대화형 모드를 통한 str 자료형의 리스트화
# st='Hello'
# print(list(st))#['H', 'e', 'l', 'l', 'o']
# #코드 3-35:for 반복문에서 문자열의 사용
# for ch in 'Hello':
#     print(ch, end=' ') #H e l l o

#중첩 for 루프
#코드 3-36: 중첩for 문을 사용한 구구단 출력
# for i in range(2,10):
#     for j in range(1,10):
#         print('{}*{}={:2d}'.format(i,j,i*j),end=' ')
#     print()
# #코드 3-37:중첩 for 루프를 이용한 패턴 만들기
# n=7
# for i in range(7): #외부 for 루프는 n번 수행, i는 0,1,2,3,4,5,6 까지 증가
#     st=''
#     for j in range(i): #내부 for 루프는 i번 수행
#         st=st + ' '    #공백을 i개 추가함
#     print(st + '#')   #공백 추가후 '#'출력
# #코드 3-38: for 루프와 *를 사용한 패턴 생성하기
# n=7
# for i in range(n): #외부 for 루프는 n번 수행, i는 0,1,2,3,4,5,6 까지 증가
#     print(' ' * i +'#')#공백 추가후 '#'출력
# #lab 3-9: 패턴 출력 응용
# n=7
# # for i in reversed(range(n)): 
# #     print(' ' * i +'#')
# for i  in range(n,-1,-1):
#     st=""
#     for j in range(i):
#         st=st+" "
#     print(st+"#")


# #상향식 문제풀이 기법
# #코드 3-39 : 4,3,2,1,0을 순서대로 출력하는 프로그램
# n=5
# for i in range(n): #i는 0,1,2,3,4 까지 증가
#     print(n-(i+1), end=' ')
# #코드 3-40 : 1,3,5,7,9를 순서대로 출력하는 시스템
# n=5
# for i in range(n):
#     print(2*i+1,end=' ')
#     """_summary_
#     """#코드 3-41: 삼각형 패턴을 출력하는 기능
# n=5
# for i in range(n):
#     for j in range(n-(i+1)):
#         print(' ',end='')
#     for j in range(2*i+1):
#         print('+',end='')
#     print()
# #코드 3-42: 삼각형 패턴을 출력하는 기능을 가진 짧은 코드
# n=5
# for i in range(n):
#     print(' '*(n-(i+1)), end=' ')
#     print('+'*(2*i+1))
# #소수 구하기
# n=int(input('수를 입력하세요 :'))
# is_prime=True
# for num in range(2,n):
#     if n%num==0:
#         is_prime=False
# print(n,'is_prime :', is_prime) #5 is_prime : True
# #코드 3-43: 2부터 100까지의 소수 구하기
# primes=[] #소수를 담을 리스트 초기화
# for n in range(2,101):
#     is_prime=True #일단 n을 소수로
#     for num in range(2,n): #2~(n-1) 사이의 수 num에 대하여
#         if n%num==0: # 이 수 중에서 n의 약수가 있으면
#             is_prime=False #소수가 아님
#     if is_prime: #소수인 경우 primes라는 리스트에 추가
#         primes.append(n) #append 메소드는 리스트에 n을 추가
# print(primes) #[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

#while 반복문
#코드 3-44: for 문을 이용한 'welcome to everyone!!'의 반복 출력기능
# for i in range(5):
#     print('Welcome to everyone!!') #Welcome to everyone!! 5번 출력
# #코드 3-45: while 문을 이용한 'Welcome to everyone!!'의 반복출력기능
# i=0
# while i<5:
#     print('Welcome to everyone!!') #Welcome to everyone!! 5번 출력
#     i+=1
# #코드 3-46: 지정된 수까지의 누적 합을 구하는 기능
# n=int(input('합계를 구할 수를 입력하세요 : '))
# s=0
# i=1
# while i <= n:
#     s=s+i
#     i+=1
# print(f'1부터 {n}까지의 합은 {s}')
#while 반복문과 입력조건
#코드 3-47: while 반복문을 이용한 가위,바위,보 선택하기
# selected=None #none은 객체의 형을 나중에 지정할 때 사용
# while selected not in ['가위','바위','보']:
#     selected= input('가위, 바위, 보 중에서 선택하세요 :')
# print('선택한 값은:',selected)
#코드 3-48: 양수 n을 입력받아 1부터 n까지의 합을 구하는 코드
# n=int(input('합계를 구할 양의 정수를 입력하세요 : '))
# s=0
# for i in range(1, n+1):
#     s=s+i
# print(f'1부터 {n}까지의 합은 {s}')
#코드 3-49: 1부터 n까지의 합을 구하는 코드로 while 문 내에서 입력문 사용
# n=-1
# while n <=0:
#     n=int(input('합계를 구할 양의 정수를 입력하세요 : '))
# s=0
# for i in range(1, n+1):
#     s=s+i
# print(f'1부터 {n}까지의 합은 {s}')

#break 와 continue
#코드 3-50: break를 사용하여 모음이 나타나면 즉시 반복문을 종료하는 기능
# st='Programming'
# for ch in st:
#     if ch in ['a','e','i','o','u']:
#         break       #P
#     print(ch)       #r
# print('The end')    #the end
# #코드 3-51 : continue를 사용하여 모음일 경우 출력을 건너뛰는 기능
# st='Programming'
# for ch in st:
#     if ch in ['a','e','i','o','u']:
#         continue       
#     print(ch)      
# print('The end')  # P r g r m m n g 줄 바꿔서 차례대로 출력후 the end   