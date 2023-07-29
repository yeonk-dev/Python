#finally구문: try:예외를 발생한 가능성이 있는 코드 except:예외가 발생했을 때 실행할 코드
#             else:예외가 발생하지 않을 때 실행할 코드 finally:무조건 실행할 코드
#finally구문:가장 마지막에 사용/예외가 발생하든 하지 않든 무조건 실행할 때 사용
try:
    number_input_a=int(input("정수 입력="))
    print("원의 반지름=",number_input_a)
    print("원의 넓이=",3.14*number_input_a**2)
except:
    print("정수를 입력해 달라고 했잖아요?!")
else:
    print("예외가 발생하지 않았습니다")
finally:
    print("일단 프로그램을 어떻게든 끝났습니다")
#try,except,finally 구문의 조합(예외 처리 구문의 규칙)
#1.try 구문은 단독으로 사용 불가, 반드시 except 구문 or finally 구문과 함께 사용해야함
#2.else 구문은 반드시 except구문 뒤에 사용해야 함
#1)try+except 구문 2)try+except+else 3)try+except+finally 4)try+except+else+finally 5)try+finally

#try+else 구문 조합(구문 오류 발생)
#try:
#    number_input_a=int(input("정수입력="))
#   print("원의 반지름=",number_input_a)
#   print("원의 넓이=",3.14*number_input_a**2)
#else:
#    print("프로그램이 정상적으로 종료되었습니다")   :SyntaxError: invalid syntax