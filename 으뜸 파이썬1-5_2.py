#1.9
print(400-200)
print(45*89)
print(32/8)
print(9*3)
print(9**3)
print(9/3)
print(9//3)
print(9%3)
#1.10
#(1)
x=1
sum=0

while x < 10:
    sum = sum + x
    x = x+1
print(sum)
#(2)
pi=3.14
r=5
print(2*pi*r)
#(3)
j=25
print(j*4)
#(4)
print(j**2)
#(5)
밑변=30
높이=10
print((밑변+높이)*2)
print(밑변*높이)

#1.11
속력=80
시간=1.5
print(속력*시간,"km")
#1.12
거리=190
시간=2
print(거리/시간,"km")
#1.13
평균거리=149597870
초당이동거리=299792
print(평균거리/초당이동거리,"초")
#1.14
def factorial(n):
    output=1    #어떤 값에 곱해도 변화가 없는 1을 초기값으로 선언
    for i in range(1,n+1):
        output*=i
    return output
print("1!=",factorial(3)) #1!=1
print("5!=",factorial(5)) #5!=120
print(factorial(12))
print(factorial(20))
#1.15
a,b=map(int,input().split())
print(f"{a}와 {b}의 평균값:{(a+b)/2}")
#1.16
a,b=map(int,input().split())
print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a/b}")


