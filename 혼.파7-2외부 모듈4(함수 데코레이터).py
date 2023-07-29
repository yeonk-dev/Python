#함수 데코레이터(decorator) : 만드는 방법에 따라 1. 함수 데코레이터 2.클래스 데코레이터
#함수 데코레이터의 기본
def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    return wrapper
#데코레이터를 붙여 함수를 만듭니다
@test
def hello():
    print("hello")

hello()
#데코레이터 사용 시 장점: functools 모듈 사용 가능/ 매개변수를 전달 할수 있어 소스의 가독성이 높여짐
from functools import wraps
def test(funtion):
    @wraps(function)
def wrapper(*arg, **kwargs):
    print("인사가 시작되었습니다")
    function(*arg,**kwargs)
    print("인사가 종료되었습니다")
    return wrapper