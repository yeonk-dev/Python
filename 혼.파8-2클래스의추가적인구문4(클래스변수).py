#클래스 변수와 메소드 (클래스가 속성(변수)과 기능(함수)을 가짐)
#클래스 변수 만들기            클래스 변수에 접근하기
#class 클래스 이름:           ♥ 클래스 이름.변수 이름
#    클래스 변수 = 값
#클래스 변수
class Student:
    count=0
    def __init__(self,name,korean,math):
        #인스턴스 함수 초기화
        self.name=name
        self.korean=korean
        self.math=math
        #클래스 변수 설정
        Student.count+=1
        print("{}번째 학생이 생성되었습니다".format(Student.count))
students=[
    Student("윤인성",87,98),
    Student("연하진",92,98),
    Student("구지연",76,96)
]
print() #클래스가 가진 기능을 명시적으로 나타내서 변수 만듦
print("현재 생성된 총 학생 수는 {}명입니다".format(Student.count)) 