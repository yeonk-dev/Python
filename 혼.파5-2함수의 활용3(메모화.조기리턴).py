#메모화
dictionary={    #메모 변수 만듦
    1:1,
    2:1
}
def fibonacci(n):   #함수 선언
    if n in dictionary:       #메모가 되어 있으면 메모된 값을 리턴
        return dictionary[n]
    else:            #메모가 되어있지 않으면 값을 구함
        output=fibonacci(n-1)+fibonacci(n-2)
        dictionary[n]=output
        return output
print("fibonacci(10)=",fibonacci(10)) #fibonacci(10)= 55
print("fibonacci(20)=",fibonacci(20)) #fibonacci(20)= 6765
#딕셔너리를 이용해서 한 번 계산한 값을 계산:메모(memo)
#처리를 수행하지 않고 곧바로 메모된 값을 돌려주면서 코드의 속도를 빠르게 만듦/"메모화"를 사용하여 결과 출력속도 up

#조기 리턴 (리턴을 중간에 사용하는 형태)
#함수 흐름의 끝에 리턴을 적음(과거 사용 형태)
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output=fibonacci(n-1)+fibonacci(n-2)
        dictionary[n]=output
        return output
print(fibonacci(10))
#조기 리턴(들여쓰기 단계를 줄임/코드를 쉽게 읽을 수 있음)
def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    output=fibonacci(n-1)+fibonacci(n-2)
    dictionary[n]=output
    return output
print(fibonacci(30))

