#끝자리로 짝수와 홀수 구분
number=input()
last_character=number[-1] #마지막 자리 숫자를 추출
last_number=int(last_character) #숫자로 변환하기
if last_number==0\  
    or last_number==2\
    or last_number==4\
    or last_number==6\
    or last_number==8:
    print("짝수입니다")

if last_number==1\
    or last_number==3\
    or last_number==5\
    or last_number==7\
    or last_number==9:
    print("홀수입니다")
#in 문자열 연산자 활용
number=input("정수 입력:")
last_character=number[-1]
if last_character in "02468":
    print("짝수입니다")
if last_character in "13579":
    print("홀수입니다")
#나머지 연산자를 활용
number=input("정수입력:")
number=int(number)
if number%2==0:
    print("짝수입니다")
if number%2==1:
    print("홀수입니다")
#실전코딩
a=float(input("첫번째숫자:"))
b=float(input("2번째숫자:"))
print()
if a>b:
    print("처음 입력했던 {}가 {}보다 더 큽니다".format(a,b))
if a<b:
    print("두 번째로 입력했던 {}가 {}보다 작습니다".format(b,a))