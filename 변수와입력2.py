#입력
string=input("입력:")
#출력
print("자료:",string)
print("자료형:",type(string))
#에러코드
#입력
string=input("입력:")
#출력
print("입력+100:",string+100)
#문자열-숫자 변환
string_a=input("입력a:")
int_a=int(string_a)
string_b=input("입력b:")
int_b=int(string_b)
print("문자열 자료:",string_a+string_b)
print("숫자자료:",int_a+int_b)

output_a:int(53)
print(type(output_a),output_a)

str_input=input("숫자입력:")
num_input=float(str_input)

print()
print(num_input,"inch")
print((num_input*2.54),"cm")

str_input=input("원의 반지름 입력:")
num_input=float(str_input)
print()
print("반지름:",num_input)
print("둘레:",2*3.14*num_input)
print("넓이:",3.14*num_input**2)
