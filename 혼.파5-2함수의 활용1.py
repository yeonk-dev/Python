#재귀함수 : 팩토리얼(factorial)
# n! = n*(n-1)*(n-2)*...*1
#반복문으로 팩토리얼 구하기
def factorial(n):
    output=1    #어떤 값에 곱해도 변화가 없는 1을 초기값으로 선언
    for i in range(1,n+1):
        output*=i
    return output
print("1!=",factorial(1)) #1!=1
print("5!=",factorial(5)) #5!=120
#재귀 함수로 팩토리얼 구하기 :재귀(recursion)-자기 자신을 호출 하는 것
#factorial(n)=n*factorial(n-1) (n>=1 일 때)
#factorial(0)=1
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print("2!=",factorial(2)) #2!=2
print("6!=",factorial(6)) #6!=720
#재귀함수 문제
#피보나치의 수열 :1번째 수열=1 /2번째 수열=1/n번째 수열=(n-1)번째 수열+(n-2)번째 수열
#재귀함수로 구현한 피보나치 수열(1)
def fibonacci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print("fibonacci(1)=",fibonacci(1)) #fibonacci(1)= 1
print("fibonacci(2)=",fibonacci(2)) #fibonacci(2)= 1
print("fibonacci(3)=",fibonacci(3)) #fibonacci(3)= 2
print("fibonacci(4)=",fibonacci(4)) #fibonacci(4)= 3
print("fibonacci(5)=",fibonacci(5)) #fibonacci(5)= 5
#시간이 다소 오래걸림 fibonacci(50)을 구할 때는 1시간이 넘게 걸림
