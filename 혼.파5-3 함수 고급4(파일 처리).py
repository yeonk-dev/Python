#파일 처리 (텍스트 파일,바이너리 파일)
#파일 열기:open() / 파일객체=open(문자열:파일 경로,문자열 :읽기 모드)
#모드 종류: w=write(새로 쓰기)/a=append(뒤에 이어서 쓰기)/r=read(읽기)
#파일 닫기: close() /파일객체.close()
file=open("basic.txt","w")
file.write("I'm pineapple")
file.close()
#with 키워드 : with open(문자열:파일 경로,문자열:모드) as 파일 객체: 문장
with open("basic.txt","w") as file:
    file.write("i'm fine") #파일에 텍스트 작성
#스트림(stream):프로그램이 외부 파일,외부 네트워크..통신할 때 데이터가 흐르는 길을 만드는 것
#with 키워드는 스트림을 열고 닫는 실수를 줄임

#텍스트 읽기(read)/파일 객체.read()
with open("basic.txt","r") as file:
    contents=file.read()
print(contents) #i'm fine
#랜덤하게 1000명의 키와 몸무게 만들기
import random
hanguls=list("가나다라마바사아자타카타파하")
with open("info.txt","w") as file:
    for i in range(100):
        name=random.choice(hanguls)+random.choice(hanguls)
        weight=random.randrange(40,100)
        height=random.randrange(140,200)
        file.write("{},{},{}\n".format(name,weight,height))
#데이터를 한 줄씩 읽어 들일 때:for 반복문/ for 한 줄을 나타내는 문자열 in 파일 객체: 처리
#반복문으로 파일 한 줄씩 읽기
with open("info.txt","r") as file:
    for line in file:
        (name,weight,height)=line.strip().split(",") #변수 선언
        if (not name)or (not weight)or (not height): #데이터 문제 확인:없으면 지나감
            continue
    bmi=int(weight)/((int(height)/100)**2) #결과 계산
    result=""
    if 25<=bmi:
        result="과체중"
    elif 18.5<=bmi:
        result="정상 체중"
    else:
        result="저체중"
    print('\n'.join([
        "이름:{}",
        "몸무게:{}",
        "키:{}",
        "BMI:{}",
        "결과:{}"
    ]).format(name,weight,height,bmi,result))
    print()