n=int(input())       #이중  for문으로 별 순서대로 출력
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()

a=int(input())
for i in range(1,a+1):
    print("*"*i,end="")
    print()

n=int(input())
for i in range(1,n+1):#행을 돌리는  for문
    for j in range(0,n-i):#공백을 돌리는 for문
        print(' ',end='')
    for k in range(i):#*을 돌리는 for문
        print('*',end='')
    print() 

n=int(input())
for i in range(n):
    for k in range(i):
        print(' ',end='')
    for j in range(n-i):
        print('*',end='')
    print() 


star=8
for k in range(1, star, 2): #1,3,5,7
    j=(star-k)/2 #1차 반복  3 2차 반복 2 3차 반복 1 
    print(" "*int(j)  ,"*"*k)

    
    

""" a=int(input())
for i in range(a,0,-1):
    print("*"*i) """


""" n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print() """


