#가변 매개변수  : def 함수 이름(매개변수,"",..,*가변 매개변수): 문장
def print_n_times(n,*values):  
    for i in range(n):        #n번 반복합니다        
        for value in values:  #values는 리스트처럼 활용합니다       
            print(value)             
        print()               #단순한 줄바꿈                  
print_n_times(2,"세븐틴","캐럿")  #함수 호출
#기본 매개변수
def print_n_times(value,n=2):
    for i in range(n):
        print(value)                     #디노
print_n_times("디노")#디노
#키워드 매개변수
#기본 매개변수가 가변 매개변수보다 앞에 올 때(의미 X)
#def print_n_times(n=2,*values):   
#  for i in range(n):           
#    for value in values:
#        print(value)          :n="안녕" valuse=["여러분","들로"] /range()함수의 매개변수에는 숫자만 가능
#    print()                   :TypeError: 'str' object cannot be interpreted as an integer
#print_n_times("안녕","여러분","들로")
#가변 매개변수가 기본 매개변수보다 앞에 올 때
def print_n_times(*values,n=2):
    for i in range(n):
        for value in values:
            print(value)             #우아해
        print()                      #하니해
print_n_times("우아해","하니해",2)    #2       :2번 반복 /가변 매개변수 우선시
#가변 매개변수와 기본 매개변수 두 가지를 한번에 사용하기 위해 "키워드 매개변수" 기능 존재
def print_n_times(*values,n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()
print_n_times("제주도","섬",n=2)
#기본 매개변수 중에서 필요한 값만 입력
def test(a,b=10,c=20):
    print(a+b+c)
test(10,20,30) #기본 형태:60
test(a=10,b=100,c=200)#키워드 매개변수로 모든 매개변수로 지정한 형태:310
test(c=10,a=100,b=200)#키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태:310
test(10,c=200)#키워드 매개변수로 일부 매개변수만 지정한 형태:220

 


