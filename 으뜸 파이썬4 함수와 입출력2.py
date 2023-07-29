#4.4 return을 이용한 반환과 튜플
#코드 4-11: 두 값의 합을 반환하는 get_sum()함수와 return 문의 사용1
def get_sum(a,b):
    result=a+b
    return result
n1=get_sum(10,20)
print('10과 20의 합=',n1) #10과 20의 합= 30
n2=get_sum(100,200)
print('100과 200의 합=',n2) #100과 200의 합= 300
#코드 4-12: 두 값의 합을 반환하는 get_sum() 함수와 return 문의 사용2
def get_sum(a,b):
    return a+b
result=get_sum(100,200)
print('두 수의 합',result) #두 수의 합 300
print('두 수의 합',get_sum(100,200)) #한 줄로 코딩
#코드 4-13: 두 값의 값을 튜플로 반환하는 방법과 전달받는 방법
def get_root(a,b,c):
    r1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    r2=(-b-(b**2-4*a*c)**0.5)/(2*a)
    return r1 ,r2
#함수 호출 시 1,2,-8 인차를 사용함
#result1,result2를 이용해서 결과 값을 반환 받는다.
result1,result2=get_root(1,2,-8)
print('해는',result1,'또는',result2) #해는 2.0 또는 -4.0
#lab 4-7: 원의 면적과 둘레를 반환하는 함수
def circle_area_circum(radius):
    r1=3.14*radius**2
    r2=2*3.14*radius
    return r1,r2
result1,result2=circle_area_circum(10)
result2="{:.1f}".format(result2)
print(f'반지름 10인 원의 면적은 {result1}, 원의 둘레는 {result2}')
#lab 4-8: 다수의 결과를 반환하는 함수 만들기
def multiples(n,m):
    r1=n*(m-3)
    r2=n*(m-2)
    r3=n*(m-1)
    r4=n*m
    return r1,r2,r3,r4
r1,r2,r3,r4=multiples(3,4)
print(r1,r2,r3,r4)

def multiples(n,m):
    r1=n*(m-4)
    r2=n*(m-3)
    r3=n*(m-2)
    r4=n*(m-1)
    r5=n*m
    return r1,r2,r3,r4,r5
r1,r2,r3,r4,r5=multiples(2,5)
print(r1,r2,r3,r4,r5)


#4.5 전역변수
#코드 4-14 : 매개변수를 사용하지 않고 외부 변수를 사용하는 경우
def print_sum():
    result=a+b
    print('print_sum() 내부 :',a, '과',b, '의 합은',result, '입니다') 
a=10
b=20
print_sum() ##print_sum() 내부 : 10 과 20 의 합은 30 입니다
result=a+b
print('print_sum() 외부 :',a, '과',b,'의 합은',result, '입니다') #print_sum() 외부 : 10 과 20 의 합은 30 입니다
#코드4-15: 함수 내부에서 값을 변경하고, 그 값을 외부 확인하기
def print_sum():
    a=100
    b=200
    result=a+b
    print('print_sum() 내부 :',a, '과',b, '의 합은',result, '입니다') 
a=10
b=20
print_sum() #print_sum() 내부 : 100 과 200 의 합은 300 입니다

#코드4-16: 함수 내부에서 값을 변경하고, 그 값을 외부에서 확인하기
def print_sum():
    a=100
    b=200
    result=a+b
    print('print_sum() 내부 ',a,'과',b,'의 합은',result, '입니다.')
a=10
b=20
print_sum() #print_sum() 내부  100 과 200 의 합은 300 입니다. #지역변수
result=a+b
print('print_sum() 외부 :',a, '과',b, '의 합은',result, '입니다')#print_sum() 외부 : 10 과 20 의 합은 30 입니다
#코드 4-17: global 키워드를 사용한 전역변수의 참조 방법
def print_sum():
    global a,b #함수 내에 사용하여 a,b는 전역변수가 되어 함수 외부에서 값을 확인해도 100,200으로 변경
    a=100
    b=200
    result=a+b
    print(f'print_sum() 내부 : {a}과 {b}의 합은 {result}입니다.')
a=10
b=20
print_sum() #print_sum() 내부 : 100과 200의 합은 300입니다.
result=a+b
print(f'print_sum() 외부: {a}과 {b}의 합은 {result}입니다') #print_sum() 외부: 100과 200의 합은 300입니다
#global 키워드는 반드시 식별자 앞에 사용해야 하며 "global a=100"-문법오류 발생한다.




