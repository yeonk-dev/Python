# strs = ["abc", "bcd", "bcdefg", "abba","cddc",'opq']
# strs=sorted(strs, key=len)
# short_len=len(strs[0])
# for i in strs:
#   if len(i)==short_len:
#     print('가장 길이가 짧은 문자열',i,end=' ')
#S=['abc','advbf','fjifjijfij','bcd','opq','jjjjjjjjjj','ggggggggg']
#S=sorted(S, key=len)
#short_len=len(S[0])
#print('길이가 가장짧은 문자열:',end=' ')
#for i in S:
#  if len(i)==short_len:
#    print(f'\'{i}\'',end=' ')
#nums=[45,67,20,34,2,100,23,45,67,89]
#평균=sum(nums)/len(nums)
#print(평균)
#시그마1=0
#for i in nums:
#  시그마1+=i*i
#시그마2=0
#for i in nums:
#  시그마2+=2*i*평균
#시그마3=0
#for i in nums:
#  시그마3+=평균*평균
#시그마총합=시그마1-시그마2+시그마3
#표준편차=(시그마총합/len(nums))**(1/2)
#print(표준편차)

def factorial(k):
    if k<=1:             
        return 1
    else:
        return 1*factorial(k-1)
print(factorial(5))
#2
def euler(n):
    d=0
    if n==0:
        return 1/0
    elif n==1:
        return 1/1
    else:
        return 1/factorial(n)