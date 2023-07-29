#재귀 함수로 구현한 피보나치 수열(2)
counter=0
def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter+=1
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

fibonacci(10)
print("---")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번 입니다.".format(counter)) #fibonacci(10) 계산에 활용된 덧셈 횟수는 109번 입니다.
#factorial(35) 계산에 활용된 덧셈 횟수는 18454929번 입니다.-덧셈 횟수가 기하 급수적으로 늘어남
#UnboundLocalError에 대한 처리 :global counter
counter=0
def finonacci(n):
    counter+=1
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10)) #UnboundLocalError: local variable 'counter' referenced before assignment
#파이썬은 함수 내부에서 외부에 있는 변수를 참조(reference:변수에 접근하는 것)하지 못함
#global 키워드-파이썬 언어에만 있는 특이한 구조
