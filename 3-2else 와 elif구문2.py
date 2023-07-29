score=float(input("학점 입력:"))
if score==4.5:
    print("신")
elif 4.2<=score:
    print("교수님의 사랑")
elif 3.5<=score:
    print("현 체제의 수호자")
elif 2.8<=score:
    print("일반인")
elif 2.3<=score:
    print("일탈을 꿈꾸는 소시민")
elif 1.75<=score:
    print("오락문화의 선구자")
elif 1.0<=score:
    print("불가촉천민")
elif 0.5<=score:
    print("자벌레")
elif 0<=score:
    print("플랑크톤")
else:
    print("시대를 앞서가는 혁명의 씨앗")
str_input=input("태어난 해를 입력해 주세요:")
birth_year=int(str_input)%12
if birth_year==0:
    print("원숭이 띠입니다")
elif birth_year==1:
    print("닭 띠입니다")
elif birth_year==2:
    print("개 띠입니다")
elif birth_year==3:
    print("돼지 띠입니다")
elif birth_year==4:
    print("쥐 띠입니다")
elif birth_year==5:
    print("소 띠입니다")
elif birth_year==6:
    print("범 띠입니다")
elif birth_year==7:
    print("토끼 띠 입니다")
elif birth_year==8:
    print("용 띠입니다")
elif birth_year==9:
    print("뱀 띠 입니다")
elif birth_year==10:
    print("말 띠입니다")
else:
    print("양 띠입니다")
x=int(input())
if 10<x<20:
    print("조건에 맞습니다")
else:
    print("탈락")