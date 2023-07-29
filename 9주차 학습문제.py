#2
for i in range(0,101,1):
    print("여기를 반복")
print(i) #반복 100번
# #3
for i in range(5,-1,-1):
    print("%d" %i)
#4
hap=0
for i in range(1,1001,5):
    hap+=i
print(hap)

#5 15단 거꾸로 출력
dan=15
for i in range(9,0,-1):
    print("%d*%d=%3d" %(dan,i,dan*i))

#6
for i in range(4):
    for j in range(3):
        for k in range(2):
            print('파이썬')


#8
s=0
hap=1234
while (hap<4568):
    if hap%444==0:
        s=hap+s
    hap=hap+1
print(s)



#9
s=0
for i in range(1,10000):
   if i%555==0:
       s=s+i
       if s>100000:
           break
   else:
       continue

print('555배수들의 합계는',s)
print('반복문 블록의 반복 횟수는',i)

