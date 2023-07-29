#실전코딩1 p.268
numbers=[1,2,3,4,5,6]
print("::".join(map(str,numbers)))  #1::2::3::4::5::6

#실전코딩2 p.269
numbers=list(range(1,10+1))

print("홀수만 추출하기")
print(list(filter(lambda numbers:numbers%2==1,numbers)))
print()
print("3 이상,7 미만 추출하기")
print(list(filter(lambda numbers:3<numbers<7,numbers)))
print()
print("제곱해서 50 미만 추출하기")
print(list(filter(lambda numbers:numbers*numbers<50,numbers)))

a, b = input().split('-')
print(a,b,sep='')

#코드업6022번
s = input()
print(s[0:2], s[2:4], s[4:6], sep=' ')
#코드업6023번
h, m, s = input().split(':')
print(m)
#코드업6024번
a,b=input().split()
s=a+b
print(s)