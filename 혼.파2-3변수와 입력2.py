#사용자 입력: input()
#input() 함수로 사용자 입력받기
string=input("인사말을 입력하세요:")
print(string)
#input()함수의 입력 자료형
number=input("숫자를 입력하세요:")
print(number)
print(type(number)) #<class 'str'>
print(type(True))   #<class 'bool'>
#입력받고 더하기
#string=input("입력:")
#print("입력+100:",string+100)  #TypeError: can only concatenate str (not "int") to str
#문자열을 숫자로 바꾸기 :int(정수) / float(실수/부동 소숫점)
str_a=input("입력a:")
int_a=int(str_a)

str_b=input("입력b:")
int_b=int(str_b)
#int()함수와 float()함수 활용하기
print("문자열 자료:",str_a+str_b)  #문자열 자료: 46
print("숫자 자료:",int_a+int_b)    #숫자 자료: 10

output_a=int("52")
output_b=float("53.224")

print(type(output_a),output_a) #<class 'int'> 52
print(type(output_b),output_b) #<class 'float'> 53.224
#int()함수와 float()함수 조합하기
input_a=float(input("첫 번째 숫자:"))
input_b=float(input("두번째 숫자:"))
print("덧셈 결과:",input_a+input_b)  #덧셈 결과: 7.0
#vlaueerror 예외
#숫자가 아닌 것을 숫자로 변환하려 할때
#print(int("안녕하세요")) #ValueError: invalid literal for int() with base 10
#소숫점이 있는 숫자 형식의 문자열을 int()함수로 변환하려 할 때

#숫자를 문자열로 바꾸기
output_c=str(87)
print("type(output_c):",type(output_c)) #type(output_c): <class 'str'>
