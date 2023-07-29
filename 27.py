#1
for j in range(5):
    for i in range(4-j):
        print(" ",end="")
    for k in range(j*2+1):
        print("*",end="")
    print()
#2

def get_max_min(data_list):
    max_val=int(data_iist[0])
    min_val=int(data_iist[0])
    for num in data_iist:
        if max_val<int(num):
            max_val=int(num)
        if min_val>int(num):
            min_val=int(num)
    return [max_val,min_val]
data_iist=list(map(int,input('입력해라:').split()))
result=get_max_min(data_iist)
print('최댓값: ',result[0],'최소값 :',result[1])

#3
def sumtest(n):
    s = 0
    for i in range(1,n+1):
        a = (n-(n-i)) * (n-(n-i))
        s = a+s
    return s

print(sumtest(10))

#4
num=int(input('숫자를 입력하세요 :'))
for i in range(num+1):
    n=[]
    for j in range(1,num+1):
        if i%j==0:
            n.append(j)
print(n)
#5
s = 0
for i in range(1, 10001):
    s += str(i).count("8")
print(s)

