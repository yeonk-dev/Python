#10진수와 2진수 변환  : bin()
print("{:b}".format(10))     #1010  : 변환했을 때 따옴표로 둘러싸여 있다면 문자열(str)자료형
print(int("1010",2))         #10 
#10진수와 8진수 변환  : : oct()
print("{:o}".format(10))     #12
print(int("12",8))           #10
#10진수와 16진수 변환   : hex()
print("{:x}".format(10))     #a
print(int("10",16))          #16