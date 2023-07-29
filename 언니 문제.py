#1
my_list=[]
for i in range(2,50+1,2):
    my_list.append(i)
print(str(my_list)[1:-1].replace(',',''))

#2
my_list_1=[11,22,23,99,81,93,35]
sum=0
for i in my_list_1:
    sum+=i
print(f'정수들의 합은 {sum}')
#3
sum=0
for i in range(1,101):
    if i%3==0:
        sum+=i
    else:
        continue
print(f'1부터 100 사이의 모든 3의 배수의 합은 {sum}입니다')
#4
num_list=[]
num=int(input('정수를 입력하시오:'))
for i in range(1,num+1):
    if num%i==0:
        num_list.append(i)
    else:
        continue
print('약수 :',str(num_list)[1:-1].replace(',',''))


#for i in range(1,n+1):
#    for j in range((n-i)):
#        print(' ',end='')
#    for k in range(i):
#        print('*',end='')
#    print()
n=int(input('정수를 입력하시오:'))
for i in (1,n+1):
    i+=1
    print(i)


a=int(input())
print(f'{a:,}')

