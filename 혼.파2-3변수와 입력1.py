#변수 만들기/사용하기
pi=3.14159265
print(pi)  #3.14159265
print(pi+2) #5.14159265
print(pi*2) #6.2831853
#원의 둘레와 넓이 구하기
pi=3.14159
r=10
print("원주율:",pi)  #원주율: 3.14159
print("반지름:",r)   #반지름: 10
print("원의 둘레:",2*pi*r)  #반지름: 10
print("원의 넓이:",pi*r*r)  #원의 넓이: 314.159
#복합 대입 연산자 :+= 숫자 덧셈 후 대입 / -= 숫자 뺄셈 후 대입 / *= 숫자 곱셈 후 대입
#                 /= 숫자 나눗셈 후 대입 / %= 숫자의 나머지를 구한 후 대입 / **=숫자 제곱 후 대입
number=100
number+=10
number+=30
print(number)  #140
string="안녕하세요"
string+="!"
string+="!"
print(string)  #안녕하세요!!
