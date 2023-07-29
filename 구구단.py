def min_pro(a,b):
    c=0
    ex=b-1
    for i in range(min(a,ex),0,-1):
        if a%i==0 and ex%i==0:
            c=a*ex/i
            break
    for i in range(min(c,b),0,-1):
        if c%i==0 and b%i==0:
            print(b*c /i)
            break
a=int(input("범위의 시작 정수 :"))
b=int(input("범위의 마지막 정수 :"))
min_pro(a,b)


