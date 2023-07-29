#4.1함수의 역할
#function(함수)
# #코드 4-1: 별표 출력을 위한 함수 정의와 호출
# def print_star():
#     print('********')

# #코드 4-2: 별표 출력을 위한 함수 정의와 반복 호출
# def print_star():
#     print('*********')
# print_star() #*********
# print_star() #*********
# print_star() #*********
# print_star() #*********
# #코드 4-3 : 3줄 별표 출력을 위한 함수 정의와 호출 방법
# def print_star3():
#     print('**')
#     print('**')
#     print('**')
# print_star3() #3줄의 별표 출력
# print_star3()
# print_star3()
# #LAB 4-2: 함수 호출 두번으로 10줄의 별표 출력
# def print_star2():
#     print('**')
#     print('**')
# print_star2()
# print_star2()
# print_star2()
# print_star2()
# print_star2()
# #코드4-4: 별표 출력을 위한 함수 정의와 호출 방법의 수정
# def print_star():
#     print('*****')
# def print_plus():
#     print('+++++')
# print_star()  #****
# print_plus()  #+++++
# print_star()  #****
# print_plus()  #+++++
# #lab4-3:함수의 정의와 호출
# #1 [코드4-4]를 수정하여 해시마크(#)를 한 줄 출력하는 print_hash()함수를 추가로 구현하시오.
# def print_hash():
#     print('#####')
# print_hash() #####
# #2 print_star(),print_plus(),print_hash() 함수를 모두 이용하여 다음과 같은 출력이 나타나도록 함수를 호출하시오
# print_hash() #####
# print_star()# *****
# print_plus()# +++++
# print_plus()# +++++
# print_star()# *****
# print_hash() #####

# #4-2 함수의 매개변수 
# #코드 4-5 :매개변수를 가진 별표 출력 함수와 인자를 이용한 호출
# def print_star(n):
#     for _ in range(n):
#         print("*****")
# print_star(4) # ****4줄 반복
# #lab 4-4 : 다양한 별표와 패턴 출력
# #코드[4-5]를 수정하여 별표줄이 10개 출력되도록 인자를 변경하시오.
# def print_star(n):
#     for _ in range(n):
#         print("*****")
# print_star(10)
# #2
# def print_hash(n):
#     for _ in range(n):
#         print("*****")
# print_hash(10)
# #3
# print_hash(6)
# #4


# #코드 4-6 : 매개변수를 사용하여 지정된 문자를 인자 값만큼 반복 출력하기
# def print_hello(n):
#     print('hello ' *n)
# print('hello를 두 번 출력합니다.') #hello를 두 번 출력합니다.
# print_hello(2) #hello hello
# print('hello를 세 번 출력합니다.') #hello를 세 번 출력합니다.
# print_hello(3) #hello hello hello
# print('hello를 네 번 출력합니다.') #hello를 네 번 출력합니다.
# print_hello(4) #hello hello hello hello
# #lab 4-5 : 두 수 연산을 수행하는 함수
# #1
# def print_sub(a,b):
#     print(f'{a}와 {b}의 차는 {a-b}입니다.')
# print_sub(10,20)
# def print_mult(a,b):
#     print(f'{a}와 {b}의 곱는 {a*b}입니다.')
# print_mult(10,20)
# #코드 4-8: 2차 방정식의 근을 구하는 기능
# a=1
# b=2
# c=-8
# r1=(-b+(b**2-4*a*c)**0.5)/(2*a)
# r2=(-b-(b**2-4*a*c)**0.5)/(2*a)
# print(f'해는 {r1}또는 {r2}') #해는 2.0또는 -4.0
#코드 4-9 : 2차 방정식의 근을 구하는 기능의 반복 사용
a=1
b=2
c=-8
r1=(-b+(b**2-4*a*c)**0.5)/(2*a)
r2=(-b-(b**2-4*a*c)**0.5)/(2*a)
print(f'해는 {r1}또는 {r2}') #해는 2.0또는 -4.0
a=2
b=-6
c=-8
r1=(-b+(b**2-4*a*c)**0.5)/(2*a)
r2=(-b-(b**2-4*a*c)**0.5)/(2*a)
print(f'해는 {r1}또는 {r2}') #해는 4.0또는 -1.0   #수식이 불필요하게 김
#코드 4-10:  2차 방정식의 근의 구하는 기능을 함수로 만들기
def print_root(a,b,c):
    r1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    r2=(-b-(b**2-4*a*c)**0.5)/(2*a)
    print(f'해는 {r1}또는 {r2}')
print_root(1,2,-8)
print_root(2,-6,-8)
#lab 4-6 : 함수의 사용
#1
def print_root(a,b,c):
    r1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    r2=(-b-(b**2-4*a*c)**0.5)/(2*a)
    print(f'해는 {r1}또는 {r2}')
print_root(1,4,-21) #해는 3.0또는 -7.0
print_root(1,-6,8) #해는 4.0또는 2.0
#2
def print_area(width,height):
    area=int((width*height)/2)
    print(f'밑변 {width},높이 {height}인 삼각형의 면적은 : {area}')
print_area(10,20)



    




