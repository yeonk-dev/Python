hello="안녕하세요"
print(hello[0:2])
print(hello)
print(len("안녕하세요"))
print("5+7=", 5+7) 
print(3/2)
print("5%2=",5%2)
print("2**2=",2**2)

number=100
number+=10
print("number:",number)
i=input("인사말을 입력하세요:")
print(i)
number=input("숫자:")
print(number)

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