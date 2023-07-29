#실전코딩1 p.89
str_input=input("숫자 입력:")
num_input=float(str_input)
print()
print(num_input,"inch")
print((num_input*2.54),"cm")

#실전코딩2 p.90
str_input=input("원의 반지름:")
num_input=float(str_input)
print()
print("반지름",num_input)
print("둘레:",2*3.14*num_input)
print("넓이:",3.14*num_input**2)

#실전코딩3 p.91 튜플(tuple)
a=input("문자열 입력:")
b=input("문자열 입력:")
print(a,b)  # 2 3
c=a
a=b
b=c
print(a,b)  # 3 2

