#2
n1,n2,n3=1,2,3
print(n1+n2*n3)
print(n1*n2+n3)
print(n1-n2*n3)
print(n1*n2-n3)

#4
num=100
num+=10
print(num)
num-=10
print(num)
num*=1
print(num)
num/=1
print(num)
num=int(num)
print(num)
print(num)
#5
num1,num2=-100,100
print(num1==num2)
print(num1>=num2)
print(num1<=num2)
print(num1!=num2)
#7(비트연산)
num1,num2=6,1
print(num1 & num2)
print(num1|num2)
print(num1 >> num2)
print(num1 << num2)
#6
num1,num2=-100,100
print((num1==num2)and (num1 != num2))
print((num1==num2)or (num1 != num2))
print((num1>=num2)and (num1 <= num2))
print((num1>=num2)or (num1 <= num2))

#9
w_500=int(input('500원 짜리 개수 :'))
w_100=int(input('100원 짜리 개수 :'))
w_50=int(input('50원 짜리 개수: '))
w_10=int(input('10원 짜리 개수:'))
print('##동전의 합계 : ',w_50*500+w_100*100+w_50*50+w_10*10)