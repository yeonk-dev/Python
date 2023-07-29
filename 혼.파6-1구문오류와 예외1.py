#오류의 종류
#구문 오류(syntax error)/실행전에 발생 : 런타임 오류(runtime errroe) or 예외(exception)/실행 중에 발생
#구문 오류(syntax error)-괄호의 개수,들여쓰기..
print("프로그램이 시작되었습니다")
#print("# 예외를 강제로 발생시켜 볼게요!) :SyntaxError: EOL while scanning string literal
print("예외를 강제로 발생시켜 볼게요!") # 예외를 강제로 발생시켜 볼게요!
#런타임 오류(runtime errroe) or 예외(exception)
print("프로그램이 시작되었습니다")
#print(list_a[1]) #NameError: name 'list_a' is not defined
list_a=[1,2,3,4,5]
print(list_a[1]) #2

#기본 예외 처리(exception handling):조건문 사용하는 방법/try 구문을 사용하는 방법
#예외 상황 확인
number_input_a=int(input("숫자 입력="))
print("원의 반지름=",number_input_a)
print("원의 넓이=",3.14*number_input_a**2) 
#"7입니다"를 넣었을 때: ValueError: invalid literal for int() with base 10: '7입니다'(정수가 아닌 경우 예외 발생)
#조건문으로 예외처리 하기(isdight()-숫자로만 구성된 글자인지 확인)
user_input_a=input("정수입력=")
if user_input_a.isdigit():
    number_input_a=int(user_input_a)
    print("원의 반지름=",number_input_a)
    print("원의 넓이=",3.14*number_input_a**2)
else:
    print("정수를 입력하지 않았습니다")
#"yes!"입력 시:"정수를 입력하지 않았습니다" 출력/프로그램이 정상으로 종료