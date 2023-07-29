#1
# print("%d / %d = %d" % (5,10,5/10)) #5 / 10 = 0
# print("%f / %f = %f" % (5,10,5/10)) #5.000000 / 10.000000 = 0.500000
# #2
# print("%04d" % 876) #0876
# print("%10s" % "Gyeongggi") #_ _Gyeongggi
# print("%3.1f" % 123.45) #123.5
# print("%10.1f" % 123.45)#_ _ _ _ _123.5
# #3
# print("{2:d} {0:05d} {1:d}".format(111,222,333))# 333 00111 222
# #4(이스케이프 문자)
# \n 줄바꿈 \t 탭(들여쓰기) \b 백스페이스 \\ 역슬래시 출력 \',\" 문자열 출력

#5(파이썬에서 제공되는 데이터 형식)
# bool , int , float, str

#6 (오류 코드)
# num1=100  
# num1=num2=100
# num1=num2=num3=100

#100= num1 - 변수의 이름은 숫자가 될 수 없음
# num1=100=num2=100 - 100에 num2를 지정할 수 없음

#7

#8

#
# s=0
# for a in range(1,100000):
#     if (a%555==0):
#         s=s+a
#         continue
#     if (a>=90450):
#         break
# print("~~~",s)
# print("~~~~",a)
# for a in range(1,100000):
#     if a%555==0:
#         s=s+a
#         if s>100000:
#             break
#     else:
#         continue
# print(s)
# print(a)
s=0
for i in range(1,100000,1):
    if i%555==0:
        s=s+i
        if s>100000:
            break
    else:
        continue
print(s)
print(i)

# s=0
# for i in range(1,100000):
#     if i%555==0:
#         s+=i
#     else:
#         pass
# print(s)



# hap=0
# for i in range(1234,4568):
#     if i %444==0:
#         hap+=i
# print(hap)
# s=0
# hap=1234
# while hap<4568:
#     if hap%444==0:
#         s=hap+s
#     hap=hap+1
# print(s)

    

        
         

    
    

        
    