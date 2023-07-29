#기본적인 함수의 활용   
#범위 내부의 정수를 모두 더하는 함수
                                   # def 함수(매개변수):
                                   # 변수=초깃값
                                   #여러가지 처리
                                   #return 변수
def sum_all(start,end):
    output=0    #초기값을 설정할 때는 연산을 해도 아무런 변화를 주지않는 것 사용(ex:0)
    for i in range(start,end+1):
     output+=i
    return output
print("0 to 100:",sum_all(0,100))  #0 to 100: 5050
#기본 매개변수와 키워드 매개변수를 활용해 범위의 정수를 구하는 함수
def sum_all(start=0,end=100,step=1):
    output=0
    for i in range(start,end+1,step):
        output+=i
    return output
print("A.",sum_all(0,100,10)) # A.550 #(10,20,30,40 ...100)
print("B.",sum_all(end=100))  # B.550 #(1,2,3,....100)
print("C.",sum_all(end=100,step=2)) # C.2550  #(0,2,4,6,8..100)
#실전코딩1-방정식을 파이썬 함수로 만들기p.226
def f(x):
    return 2*x+1     #f(x)=2x+1
print(f(10))
def f(x):
    return x**2+2*x+1  #f(x)=x**2+2x+1
print(f(10))
#실전코딩2 p.227
def mul(*values):
        output=1
        for value in values:
            output*=value
        return output
print(mul(5,7,9,10))
#실전코딩3
def funtion(valuea,valueb,*values):
    pass
funtion(1,2,3,4,5)
def funtion(*values,valuea,valueb):
    pass
function(1,2,3,4,5)
def funtion(valuea=10,valueb=20,*values):
    pass
function(1,2,3,4,5)