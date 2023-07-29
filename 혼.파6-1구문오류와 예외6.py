#index():리스트 내부의 특정 값이 어디 있는 지 확인
numbers=[52,375,8,96,10]
print(numbers.index(375)) #1
#해당 값이 여러 개 있을 경우 첫 번째 값의 위치 리턴
numbers=[1,1,1,1,1,1]
print(numbers.index(1)) #0
#리스트의 없는 값에 접근하여 할때
#numbers=[52,375,8,96,10]
#print(numbers.index(10000)) #ValueError: 10000 is not in list
#실전 코딩1
numbers=[52,273,32,103,90,10,275]
print("#(1)요소 내부에 있는 값 찾기")
print("-{}는 {}위치에 있습니다.".format(52,numbers.index(52)))
print()
print("(2) 요소 내부에 없는 값 찾기")
number=10000
try:
    if number in numbers:
        print("-{}는 {}위치에 있습니다.".format(number,numbers.index(number)))
    else:
        print("리스트 내부에 없는 값 입니다")
except:
    pass

print()

print("---정상적으로 종료되었습니다---")

#(2)
numbers=[52,273,32,103,90,10,275]
print("#(1)요소 내부에 있는 값 찾기")
print("-{}는 {}위치에 있습니다.".format(52,numbers.index(52)))
print()
print("(2) 요소 내부에 없는 값 찾기")
number=10000
if number in numbers:
    print("-{}는 {}위치에 있습니다.".format(number,numbers.index(number)))
else:
    print("리스트 내부에 없는 값 입니다")

print()

print("---정상적으로 종료되었습니다---")