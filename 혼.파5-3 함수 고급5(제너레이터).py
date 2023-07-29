#제너레이터(generator): 함수내부에 yield 키워드를 사용함 / 이터레이터를 직접 만들때 사용하는 코드(p.204)
#제너레이터함수
def test():
    print("함수가 호출되었습니다")
    yield "test"
print("A지점 통과")
test()               #A지점 통과
print("B지점 통과")
test()               #B지점 통과
print(test())        #<generator object test at 0x000001FD01DFBB10> (제너레이터 객체)
#원래 test()를 호출하면 "함수가 호출되었습니다"라는 문자열이 호출되어야함
#=제너레이터 함수는 제너레이터를 리턴함
#제너레이터 객체와 next()함수:next()함수의 리턴값으로 yield키워드 뒤에 입력한 값이 출력됨
def test():
    print("A지점 통과")
    yield 1
    print("B지점 통과")
    yield 2
    print("C지점 통과")
output=test()
print("D지점 통과") #D지점 통과
a=next(output)     #A지점 통과
print(a)           #1
print("E지점 통과") #E지점 통과
b= next(output)    #B지점 통과
print(b)           #2
print("F지점 통과") #F지점 통과
#c=next(output)     #C지점 통과
#print(c)           #StopIteration :next()함수 호출한 이후 yield 키워드를 만나지 못하고 끝나면 발생
#next(output)

#실전코딩1 p.268
numbers=[1,2,3,4,5,6]
print("::".join(map(str,numbers)))  #1::2::3::4::5::6
#실전코딩2 p.269
numbers=list(range(1,10+1))

print("홀수만 추출하기") #홀수만 추출하기
print(list(filter(lambda numbers:numbers%2==1,numbers))) #[1, 3, 5, 7, 9]
print()
print("3 이상,7 미만 추출하기") #3 이상,7 미만 추출하기
print(list(filter(lambda numbers:3<numbers<7,numbers)))#[4,5,6]
print()
print("제곱해서 50 미만 추출하기") #제곱해서 50 미만 추출하기
print(list(filter(lambda numbers:numbers*numbers<50,numbers)))#[1,2,3,4,5,6,7]
  
