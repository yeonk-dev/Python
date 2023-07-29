#CustomException
#사용자 정의 예외 클래스 만들기
class CustomException(Exception): 
    def __init__(self):           #Traceback (most recent call last):
        Exception.__init__(self)  # File "c:\Users\USER\Desktop\파이썬\혼.파8-2상속2(예외 클래스 만들기).py", line 7, in <module>
                                  #raise CustomException     
raise CustomException             #__main__.CustomException

#자식 클래스로써 부모의 함수 재정의(오버라이드)하기
class CustomException(Exception):
    
        