#모든 예외 잡기(except 구문으로 예외를 구분하면 if, elif, else 조건문 처럼 차례대로 오류 검출하면서 확인)
#예외 처리를 했지만 예외를 못 잡는 경우
list_number=[52,273,32,72,100]
try:
    number_input=int(input("정수 입력="))
    print("{}번째 요소: {}".format(number_input,list_number[number_input]))
    예외.발생해주세요()
except ValueError as exception:
    print("정수를 입력해 주세요!")
    print(type(exception),exception)   #Traceback (most recent call last):  
except IndexError as exception:      #File "c:\Users\USER\Desktop\파이썬\혼.파6-2 예외 고급2.py", line 7, in <module>
    print("리스트의 인덱스를 벗어났어요!")# 예외.발생해주세요()
    print(type(exception),exception) #NameError: name '예외' is not defined  -프로그램 종료
#모든 예외 잡기
list_number=[52,273,32,72,100]
try:
    number_input=int(input("정수 입력="))
    print("{}번째 요소:{}".format(number_input,list_number[number_input]))
    예외.발생해주세요()
except ValueError as exception:    
    print("정수를 입력해주세요!")    
    print(type(exception),exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print(type(exception),exception)
except Exception as exception:
    print("미리 파악하지 못한 예외가 발생했습니다.") 
    print(type(exception),exception)  
#정수 입력시                                    문자열 입력시
#정수 입력=1                                    정수 입력=yes                         
#1번째 요소: 273                                정수를 입력해 주세요!
#미리 파악하지 못한 예외가 발생했습니다            <class 'ValueError'> invalid literal for int() with base 10: 'yes'
#<class 'NameError'> name '예외' is not defined

#인덱스가 넘은 정수 입력시 (5 이상)
#정수 입력=100
#리스트의 인덱스를 벗어났어요!
#<class 'IndexError'> list index out of range

#아직 구현되지 않은 부분에서 강제로 예외 발생시키기
number=input("정수 입력:")
number=int(number)
if number>0:
    raise NotImplementedError
else:
    raise NotImplementedError 
#raise 예외 객체:아직 구현되지 않은 부분을 일부러 예외를 발생시켜 프로그램을 죽게 만들어 잊어버리지 않게 하는 기능
#  