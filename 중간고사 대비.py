# def 진약수구하기():
#     for i in range(1,10000+1):
#         약수모음=[]
#         #약수 리스트에 넣는 알고리즘
#         for j in range(1,i):
#             if i%j==0:
#                 약수모음.append(j)
#         if sum(약수모음)==i:
#             sums=sum(약수모음)
#             print(f'{i}는 완전수입니다.')
#             print(f'{i}의 약수:{약수모음},약수의 합{sums}')
            
# 진약수구하기()

n=int(input())
l1=[]
for i in range(1,n*n+1):
    l1.append(i)
for j in range(0,n*n,5):
    if j%2==0:
        l2=l1[j:j+5]
        for i in l2:
            print(f'{i}\t',end='')
        print()
    else:
        l2=l1[j+4:j-1:-1]
        for i in l2:
            print(f'{i}\t',end='')
        print()


    