n=int(input('입력 : '))
for i in range(1,n+1):
    if (i%2==1):
        for j in range(n*(i-1)+1,n*(i)+1):
            print(f'{j}\t',end='')
        print()
    else:
        for j in range(n*(i),n*(i-1),-1):
            print(f'{j}\t',end='')
        print()









