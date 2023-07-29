#비교연산자
# == 같다 != 다르다 < 작다 > 크다 <=작거나 같다 >= 크거나 같다
print(10==100) #false
print(10<=100) #true
#문자열 비교연산자 (사전순서)
print("사진"=="사진") #true
print("사진"<"모자") #false
#범위구하기
x=int(input()) 
print(10<x<30) #true
print(40<x<60) #false
#불연산하기:논리연산자
#not:아니다:불을 반대로 전환합니다(단항 연산자)
print(not True) #false
print(not False)#true
x=10
under_20=x<20
print("under:",under_20)
print("not under_20:",not under_20) #not under
#and연산자:양쪽 변의 값이 모두 참일때만 true
#or연산자:둘 중 하나만 참이여도 true
print(True and True) #true
print(True and False) #true
print(False or False) #false