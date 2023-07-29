# import pandas as pd
# a=pd
# b=pd
# a=a.DataFrame
# print(a)

#리스트 항목 값 변경
a=[1,2,3,3]
a[2]=5
print(a) #[1, 2, 5, 3]
#리스트 요소 출력
for i in range(3):
    print(a[i])  #1, 2  5 줄바꿔 출력
x=[10,20,30,40]
for i in range(0,4,1):
    print(i,":",x[i])
#if 키워드 in 리스트
f=['apple',"orange","kiwi"]
if "apple" in f:
    print('사과가 있습니다') #사과가 있습니다
#길이출력 len
for i in range(len(x)):
    print(f'{i}:{x[i]}')
#합계
print(sum(x))
#평균
print(int(sum(x)/len(x)))
#print(i,x[i],sep='')
#print(i,x[i],sep='^^',end="&&")
for s in [5,6,7,8]:
    print(s)
#리스트에 값 추가/삭제
x.append(50)
print(x) #[10, 20, 30, 40, 50]
x.insert(1,500)
print(x) #[10, 500, 20, 30, 40, 50]
x.remove(20) #원소의 값을 적어 삭제
print(x) #[10, 500, 30, 40, 50]
x.pop(3) #인덱스 번호로 삭제
print(x) #[10, 500, 30, 50]

