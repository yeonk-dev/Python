#구문 내부에 여러 줄 문자열을 사용할 때
number=int(input("정수 입력:"))
if number%2==0:                                     
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 짝수입니다.""".format(number,number))
else:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 홀수입니다.""".format(number,number))        #들여쓰기(indent)가 들어감

number=int(input("정수 입력:"))
if number%2==0:                                     
    print("""입력한 문자열은 {}입니다.
{}는(은) 짝수입니다.""".format(number,number))
else:
    print("""입력한 문자열은 {}입니다.                         
{}는(은) 홀수입니다.""".format(number,number))               #들여쓰기는 없음. but 코드 구조 이상/복잡

number=int(input("정수 입력:"))
if number%2==0:
    print("입력할 문자열은 {}입니다.\n{}는 짝수입니다".format(number,number))
else:
    print("입력할 문자열은 {}입니다.\n{}는 홀수입니다".format(number,number))  #깔끔한 구조
#괄호로 문자열 연결
test=(
    "이렇게 입력해도"
    "하나의 문자열로"
    "생성됩니다"
)
print("test:",test)                 #test: 이렇게 입력해도하나의 문자열로생성됩니다
print("type(test):",type(test))     #type(test): <class 'str'>
#튜플 자료형
test=(
    "쉼표로 연결하면",
    "문자열이 아니라 ",
    "튜플이 완성됩니다."
)
print(test)    #('쉼표로 연결하면', '문자열이 아니라 ', '튜플이 완성됩니다.')
# \n :줄바꿈을 위해 마지막을 제외한 문자열 뒤에 입력
number=int(input("정수 입력:"))
if number%2==0:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는 짝수입니다"
    ).format(number,number))
else:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는 홀수입니다"
    ).format(number,number))

