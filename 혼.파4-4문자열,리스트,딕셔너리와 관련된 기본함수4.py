#join():문자열.join(문자열로 구성된 리스트)
print("::".join(["1","2","3","4","5"]))    #1::2::3::4::5
number=int(input("정수 입력:"))
if number%2==0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는 짝수입니다"
    ]).format(number,number))
else:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는 홀수입니다"
    ]).format(number,number))
#이터러블iterable(반복할 수 있는 것/내부에 있는 요소를 차례로 꺼낼 수 있는 객체)
#이터레이터iterator(이터러블 중에 next()함수를 적용해 하나하나 꺼낼 수 있는 요소)
numbers=[1,2,3,4]
r_num=reversed(numbers)
print("reversed_number:",r_num) #reversed_number: <list_reverseiterator object at 0x000002814170D1D0>
print(next(r_num))  #4
print(next(r_num))  #3
print(next(r_num))  #2
print(next(r_num))  #1
