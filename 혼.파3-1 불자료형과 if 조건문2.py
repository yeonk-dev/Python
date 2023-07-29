#if 불 값이 나오는 표현식:
#----불 값이 참일때 실행할 문장: 4칸 들여쓰기 후 입력
if False:
    print("false입니다...!") #if뒤에있는 불 값이 거짓인 경우는 아무것도 실행되지 않음
if True:
    print("사실입니다") #사실입니다 실행
#조건문의 기본사용
number=input("정수 입력:")
number=int(number)
if number>0:
    print("양수입니다")
if number<0:
    print("음수입니다")
if number==0:
    print("0입니다")
#날짜/시간 출력
import datetime #날짜.시간과 관련된 기능 가져오기
now=datetime.datetime.now() #현재 날짜 시간 구하기
print(now.year,"년")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")
#한 줄로 출력
import datetime
now=datetime.datetime.now()
print("{}년{}월{}일{}시{}분".format(now.year,now.month,now.day,now.hour,now.minute))
#오전/오후 구분
import datetime
now=datetime.datetime.now()
if now.hour<12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))
if now.hour >=12:
    print("현재 시각은 {}시로 오후입니다".format(now.hour))
#계절을 구분하는 프로그램
import datetime
now=datetime.datetime.now()
if 3<=now.month <=5:
    print("이번 달은{}월로 봄입니다".format(now.month))
if 5<=now.month<=8:
    print("이번 달은{}월로 여름입니다".format(now.month))
if 9<=now.month<=11:
    print("이번 달은{}월로 가을입니다".format(now.month))
if 12 or 1<=now.month<=2:
    print("이번 달은 {}월로 겨울입니다".format(now.month))