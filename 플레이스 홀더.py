def pic_out(n):
    for i in range(n):
        print("#",end='')
    print()
num=input('여러 개의 숫자를 입력하시오:')
for n in num:
    pic_out(int(n))