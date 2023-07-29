#객체를 처리하는 함수(2)
def create_student(name,korean,math): #딕셔너리를 리턴하는 함수 만들기
    return {
        "name":name,
        "korean":korean,
        "math":math
    }
def student_get_sum(student):                   #학생을 처리하는 함수 만들기
        return student["korean"]+student["math"]
def student_get_average(student):
        return student_get_sum(student)/2
def student_to_string(student):
    return"{}\t{}\t{}".format(student["name"],
        student_get_sum(student),
        student_get_average(student))
students=[                            #학생 리스트를 선언합니다
    create_student("윤인성",87,98),
    create_student("연하진",92,98),
    create_student("구지연",76,96)
]
print("이름","총점","평균",sep="\t") #학생을 한 명씩 반복
for student in students:
    print(student_to_string(student)) #출력

#클래스를 선언하기
# class 클래스 이름 : 클래스 내용
#인스턴스 이름(변수 이름) = 클래스 이름() ----> 생성자 함수!! 
#인스턴스(instance): 클래스를 기반으로 만들어진 객체

#클래스를 선언합니다
class Student:
    pass
#학생을 선언합니다
student=Student()
#학생 리스트를 선언합니다
students=[
    Student(),
    Student(),
    Student(),
    Student()
]


