#false로 변환되는 값
print("#if조건문에 0 넣기")
if 0:
    print("0은 True로 변환됩니다")
else:
    print("0은 False로 변환됩니다")
print()

print("#if 조건문에 빈 문자열 넣기")
if"":
    print("빈 문자열은 True로 변환됩니다")
else:
    print("빈 문자열은 False로 변환됩니다")
#pass키워드
x=10
y=2
if x>4:
    if y>2:          #출력없음
        print(x*y)
else:
    print(x+y)