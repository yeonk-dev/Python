#datetime 모듈
import datetime
print("#현재 시각 출력하기")
now=datetime.datetime.now()
print(now.year,"년")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")
#시간출력 방법
print("시간을 포맷에 맞춰 출력하기")
output_a=now.strftime("%Y.%m.%d %H:%M:%S")
output_b="{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\
    now.month,\
    now.day,\
    now.hour,\
    now.minute,\
    now.second)
output_c=now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
print(output_a)
print(output_b)
print(output_c)

#시간 처리하기
import datetime
now=datetime.datetime.now()
print("#datetime.timedelta로 시간 더하기")
after=now+datetime.timedelta(\
    weeks=1,\
    days=1,\
    hours=1,\
    minutes=1,\
    seconds=1)
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
print()
#특정 시간 요소 교체하기
print("# now.replace()로 1년 더하기")
output=now.replace(year=(now.year+1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
#timedelta():특정한 시간 이전/이후를 구함:몇 년후를 구하는 기능 없음/replace()함수를 이용해 아예 날짜 값을 교체

#time모듈 : import time :유닉스 코드/특정시간 동안 정지하는 기능(time.sleep() 자주 사용)
import time
print("지금부터 5초 동안 정지합니다!")
time.sleep(5)
print("프로그램을 종료합니다")