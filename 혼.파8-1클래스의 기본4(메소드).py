#메소드(method): 클래스가 가지고 있는 함수
#class 클래스 이름:
#  def 메소드 이름(self, 추가적인 매개변수):
#     pass
# "C#","Java"=클래스의 함수 '메소드'/ 파이썬="멤버 함수(member function)" or "인스턴스 함수(instance funtion)"

#클래스 내부 함수(메소드) 선언하기
class Student:
    def __init__(self,name,korean,math):
        self.name=name
        self.korean=korean
        self.math=math
    def get_sum(self):
        return self.korean+self.math
    def get_average(self):
        return self.get_sum()/2
    def to_string(self):
        return"{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())
Students=[
    Student("윤인성",87,98),
    Student("연하진",92,98),
    Student("구지연",76,96)
]
print("이름","총점","평균",sep="\t")
for student in Students:
    print(student.to_string())
