n=input() #처음 숫자
sum=0 # 숫자 분리해서 합 구하는거
k=0 #돌린 횟수
list_each=[] #각각분리해서 넣을 리스트

for i in n:
    print(i)
    i=int(i)
    list_each.append(i)
b=list_each[1]
for j in list_each:
    sum+=j
    k+=1
if sum==n:
    print(k)
else:
    

    

    


