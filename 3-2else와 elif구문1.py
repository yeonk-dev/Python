#else조건문
#if 조건: 조건이 실행될때 실행할 문장
#else 조건: 조건이 거짓일때 실행할 문장
#if+else 구문 추가해서 짝수 홀수 구분
number=input("정수입력:")
number=int(number)
if number%2==0:
    print("짝수입니다")
else:
    print("홀수입니다")
#elif:세 개 이상의 조건을 연결해서 사용하는 방법
#계절구하기
import datetime
now=datetime.datetime.now()
month=now.month
if 3<=now.month <=5:
    print("현재는 봄 입니다")
elif 6<=now.month<=8:
    print("현재는 여름 입니다")
elif 9<=now.month<=11:
    print("현재는 가을 입니다")
else :
    print("현재를 겨울 입니다")