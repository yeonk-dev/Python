#10진수와 2진수 변환  : bin()
print("{:b}".format(10))     #1010  : 변환했을 때 따옴표로 둘러싸여 있다면 문자열(str)자료형
print(int("1010",2))         #10 
#10진수와 8진수 변환  : : oct()
print("{:o}".format(10))     #12
print(int("12",8))           #10
#10진수와 16진수 변환   : hex()
print("{:x}".format(10))     #a
print(int("10",16))          #16
#추가로 반복 가능한 객체(문자열,리스트,범위..) :count()
print("쎄이쎄이호오".count("쎄"))   #2
#실전코딩1 : 1-100사이에 있는 숫자 중 2 진수로 변환했을 때 0이 하나만 포함된 숫자를 찾고
#그 숫자들의 합을 구하는 코드 만들기
output=[i for i in range(1,100+1)
if "{:b}".format(i).count("0")==1]
for i in output:
    print("{}:{}".format(i,"{:b}".format(i)))
print("합계:",sum(output))
