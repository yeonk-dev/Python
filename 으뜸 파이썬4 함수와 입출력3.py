#4.6 함수의 인자전달 방식
#4.6.1 디폴트 인자
#코드 4-18: 인자를 빠뜨린 호출
# def print_star(n): #인자를 하나 필요로 함
#     for _ in range(n):
#         print('*****')
# print_star() # 인자가 없으므로 에러 발생 #TypeError: print_star() missing 1 required positional argument: 'n'
#디폴트 값(기본 값)을 사용하여 유연성 있는 작업/ 디폴트 인자
#코드 4-19: 디폴트 값을 가지는 print_star() 함수
# def print_star(n=1):
#     for _ in range(n):
#         print("******")
# print_star() #******
# print_star(2)   #****** 2줄 출력
# #코드 4-20: 디폴트 인자를 1개 사용한 div() 함수
# def div(a,b=2):
#     return a/b
# print('div(4) =',div(4)) #div(4) = 2.0
# print('div(6,3) =',div(6,3)) #div(6,3) = 2.0
# #코드4-21: 매개변수에 디폴트 값을 2개 사용한 div() 함수
# def div(a=1,b=2):
#     return a/b
# print(div()) #div(1,2) #0.5
# print(div(4)) #div(4,2) #2.0
# print(div(6,3)) #div(6,3) #2.0

#4.6.2 키워드 인자
#코드 4-22: 2차 방정식의 근을 구하는 함수와 함수 호출문
# def get_root(a,b,c):
#     r1=(-b+(b**2-4*a*c)**0.5)/(2*a)
#     r2=(-b-(b**2-4*a*c)**0.5)/(2*a)
#     return r1,r2                     #함수 호출시 1,2,-8 인자를 사용함
# result1,result2=get_root(1,2,-8)     #result1,result2 이용하여 결과 값을 반환받는다
# print(f'해는 {result1} 또는 {result2}') #해는 2.0 또는 -4.0

# def get_root(a,b,c):
#     r1=(-b+(b**2-4*a*c)**0.5)/(2*a)
#     r2=(-b-(b**2-4*a*c)**0.5)/(2*a)
#     return r1,r2                     #함수 호출시 1,2,-8 인자를 사용함
# result1,result2=get_root(a=1,b=2,c=-8)     #result1,result2 이용하여 결과 값을 반환받는다
# print(f'해는 {result1} 또는 {result2}') #인자의 값을 지정하여 호출시 의미 명확히 함
#에러유형1 [키워드 인자 뒤에서 위치 인자를 사용한 경우]
# def get_root(a,b,c):
#     r1=(-b+(b**2-4*a*c)**0.5)/(2*a)
#     r2=(-b-(b**2-4*a*c)**0.5)/(2*a)
#     return r1,r2                    
# result1,result2=get_root(c=-8,b=2,1) #SyntaxError: positional argument follows keyword argument  
# print(f'해는 {result1} 또는 {result2}') #키워드 인자의 뒤에 위치 인자를 사용할 수 없음
#에러유형2 [같은 위치에 할당된 값을 뒤에 키워드 인자로 할당해 줄 경우]
# def get_root(a,b,c):
#     r1=(-b+(b**2-4*a*c)**0.5)/(2*a)
#     r2=(-b-(b**2-4*a*c)**0.5)/(2*a)
#     return r1,r2                    
# result1,result2=get_root(1,-8,b=2) #TypeError: get_root() got multiple values for argument 'b' 
# print(f'해는 {result1} 또는 {result2}') #b가 여러번 할당 된 것으로 인식함
#코드4-23: 직사각형과 원의 면적을 구하는 함수의 구현
def func(shape,width=1,height=1,radius=1):
    if shape==0:  #shape 값이 0이면 사각형의 면적을 반환
        return width*height
    if shape==1:  #shape 값이 1이면 원의 면적을 반환
        return 3.14*radius**2
print('rect area=',func(0,width=10,height=2)) #rect area= 20
print('circle area=',func(1,radius=5)) #circle area= 78.5
#lab 4-9:키워드 인자
def print_name(honorifics,first_name,last_name):
    print(honorifics,first_name,last_name)
print_name(first_name='glidong',last_name='hong',honorifics='dr.') #dr. glidong hong
print_name('gildong','hong','dr.') #gildong hong dr.
#4.6.3 가변적인 인자전달
#코드 4-24: 인자를 하나 가지는 함수
def greet1(name):
    print('안녕하세요',name,'씨')
greet1('장원영') #안녕하세요 장원영 씨
#코드 4-25: 인자를 2개 가지는 함수
def greet2(name1,name2):
    print('안녕하세요',name1,'씨')
    print('안녕하세요',name2,'씨')
greet2('이영지','안유진') #안녕하세요 이영지 씨  /안녕하세요 안유진 씨 두 줄 출력
#코드 4-26: 가변 인자를 가지는 함수의 정의와 호출
def greet(*names):
    for name in names:
        print('안녕하세요',name, '씨')
greet('홍길동','김레이') #안녕하세요 홍길동 씨 /안녕하세요 김레이 씨
greet('James','ellen') #안녕하세요 James 씨 / 안녕하세요 ellen 씨
#코드 4-27: 가변 인자를 가지는 함수에서 len() 함수 활용
def foo(* args):
    print('인자의 개수:',len(args)) #인자의 개수: 3
    print('인자들:',args) #인자들: (10, 20, 30)
foo(10,20,30)
#코드 4-28: 가변 인자를 가지는 함수를 이용한 합계 구하기
def sum_nums(*numbers):
    result=0
    for n in numbers:
        result +=n
    return result
print(sum_nums(10,20,30)) #60
print(sum_nums(10,20,30,40,50)) #150
#lab 4-10: 가변 인자의 활용
#1
def sum_nums(numbers):
    result=0
    result1=0
    len1=len(numbers)
    result=sum(numbers)
    result1=result/len1
    return result,result1,len1
numbers=(10,20,30,40,50)
r1,r2,l1=sum_nums(numbers)
print(f'''
{l1}개의 인자 {numbers}
합계: {r1} 평균:{r2}
'''.strip())
#2
# def min_nums(*numbmers):
#     print('최소값은 ',min(numbmers))
# min_nums(20,40,50,10)
