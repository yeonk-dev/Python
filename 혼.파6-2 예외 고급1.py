#예외 객체(exception object)
#try: 예외가 발생할 가능성이 있는 구문
#except 예외의 종류 as 예외 객체를 활용할 변수 이름: 예외가 발생했을 때 실행할 구문
#"Exception" -클래스
try: #try except 구문으로 예외 처리
    number_input_a=int(input("정수 입력:"))
    print("원의 반지름:",number_input_a)
    print("원의 둘레:",2*3.14*number_input_a)
except Exception as exception:
    print("type(exception):",type(exception)) #예외 객체 출력
    print("exception:",exception)
    #yes! 입력 시 exception: invalid literal for int() with base 10: 'yes'
#예외 구분하기(except 구문을 if 조건문처럼 사용해서 예외구분)
#여러 가지 예외가 발생할 수 있는 코드
list_number=[52,273,32,72,100]
try:
    number_input=int(input("정수 입력="))
    print("{}번째 요소: {}".format(number_input,list_number[number_input]))
except Exception as exception:
    print("type(exception):",type(exception))
    print("exception:",exception)
#"정수로 변환될 수 없는 값 입력"-(ValueError) exception: invalid literal for int() with base 10: 'yes'
#"정수를 입력하지만,리스트의 길이를 넘는 인덱스 입력"-(IndexError)exception: list index out of range

#예외 구분하기
list_number=[52,273,32,72,100]
try: #try except 구문으로 예외 처리
    number_input=int(input("정수 입력="))
    print("{}번째 요소: {}".format(number_input,list_number[number_input]))
except ValueError:                                 #ValueError 발생 경우
    print("정수를 입력해 주세요")
except IndexError:                                 #IndexError 발생 경우
    print("리스트의 인덱스를 벗어났어요!")
#예외 구분 구문과 예외 객체 (except 구문뒤에 예외 객체를 붙여 활용 가능)
list_number=[52,273,32,72,100]
try: 
    number_input=int(input("정수 입력="))
    print("{}번째 요소: {}".format(number_input,list_number[number_input]))
except ValueError as exception:                               
    print("정수를 입력해 주세요") #정수를 입력해 주세요
    print("exception:",exception) #exception: invalid literal for int() with base 10: 'yes'
except IndexError:                                
    print("리스트의 인덱스를 벗어났어요!") #리스트의 인덱스를 벗어났어요!
    print("exception:",exception) #IndexError: list index out of range