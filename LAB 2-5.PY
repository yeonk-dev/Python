#lab 2-5 :다양한 식별자를 활용한 변수 활용
#1.
#global=300
#print(global) #SyntaxError: invalid syntax (파이썬 키워드는 사용 용도가 고정되어 변수로 사용 불가능)
#2.
# width=20
# height=40
# area=(width*Height)  ==NameError: name 'Height' is not defined
# print('사각형의 면적',area)
width=20
height=40
area=(width*height)  
print('사각형의 면적:',area)
#3.
iixxjjkk=20
print('나의 나이는',iixxjjkk,'세 입니다') #변수 이름이 명확하지 않음
#4
v1=1
v2=2
thisissaverylongvariablename= v1+v2
print(thisissaverylongvariablename) ##변수 이름이 명확하지 않음/ 이름이 너무 길음
#5
radius=20
depth=10
final_length=0.5*radius*depth
print('삼각형의 면적은',final_length)
#6.
# 1st_year=30
# 2st_year=30
# all_year+=1st_year+2st_year
# print(all_year+)  SyntaxError: invalid syntax (숫자 1로하는 식별자는 사용 불가능)
