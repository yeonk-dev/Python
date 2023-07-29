#C를 제외항 모든 프로그래밍 언어는 "객체 지향 프로그래밍 언어(Object Oriented Programming Languege)"
#객체를 우선으로 생각해서 프로그래밍/ 클래스(class) 기반으로 객체(object) /★데이터(data)★
#추상화(abstraction): 필요한 요소만을 사용해서 객체를 표현하는 것
#딕셔너리로 객체 만들기
students=[
    {"name":"윤인성","korean":87,"math":98},
    {"name":"연하진","korean":92,"math":98},
    {"name":"구지연","korean":76,"math":96}
]
print("이름","총점","평균",sep="\t")
for student in students:
    score_sum=student["korean"]+student["math"]
    score_average=score_sum/2
    print(student["name"],score_sum,score_average,sep="\t")
#객체(object):여러 가지 속성을 가질 수 있는 대상 (ex:학생)
#객체를 만드는 함수(1)
def create_student(name,korean,math): #딕셔너리를 리턴하는 함수 만들기
    return {
        "name":name,
        "korean":korean,
        "math":math
    }        
student=[                           #학생 리스트를 선언
    create_student("윤인성",87,98),
    create_student("연하진",92,98),
    create_student("구지연",76,96)
]
print("이름","총점","평균",sep="\t") #학생을 한 명씩 반복
for student in students:
    score_sum=student["korean"]+student["math"] #점수의 총합과 평균 구하기
    score_average=score_sum/2
    print(student["name"],score_sum,score_average,sep="\t") #출력