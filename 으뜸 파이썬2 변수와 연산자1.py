#파이썬의 출력 함수 print()
print("Hello Python!!")
#print(Hello Python!!) #SyntaxError: invalid syntax
print('My age is', 20) #My age is 20
print('오늘의 걸음 수',8000, '걸음') #오늘의 걸음 수 8000 걸음
print('Hello ' *2) #Hello Hello

print('나의 이름은 :','홍길동')
print('나의 나이는 :', 27)
print('나의 키는', 179, 'cm 입니다.')
print('10+20 =', 10+20)
print('10*20 =', 10*20)

#변수와 친해지기
#원의 반지름,면적,둘레 출력
print('원의 반지름', 4.0)
print('원의 면적', 3.14*4.0*4.0)
print('원의 둘레', 2.0*3.14*4.0)

pi=3.14
r=int(input())
print('원의 반지름', r)
print('원의 면적', pi*r*r)
print('원의 둘레', 2.0*pi*r)

#코드 2-3 : 변수를 이용하여 원의 면적과 둘레를 구하는 방법
radius= 4.0
print('원의 반지름', radius)
print('원의 면적', 3.14*radius*radius)
print('원의 둘레', 2.0*3.14*radius)
radius= 6.0
print('원의 반지름', radius)
print('원의 면적', 3.14*radius*radius)
print('원의 둘레', 2.0*3.14*radius)