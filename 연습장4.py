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
import datetime #날짜.시간과 관련된 기능 가져오기
now=datetime.datetime.now() #현재 날짜 시간 구하기
print(now.year,"년")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")