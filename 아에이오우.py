a=int(input("줄개수"))
start=2*a-1
for i in range(a):
    print('.',i,"*"*(start-2*i))