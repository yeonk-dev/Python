#리턴
value=input(":")  #input()함수의 리턴값을 변수에 저장장
print(value)
#자료 없이 리턴하기
#함수 내부에 return 의미:함수를 실행했던 위치로 돌아가라=함수가 끝나는 위치
def return_test():
    print("최애 입니다")
    return
    print("차애입니다")
return_test()     #최애 입니다
#자료와 함께 리턴하기
def return_test():
    return 100
value=return_test()
print(value)      #100
#아무것도 리턴하지 않기
def return_test():
    return
value=return_test()
print(value)        #None(없다)