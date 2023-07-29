#상속: 어떤 클래스를 기반으로 속성과 기능을 물려받아 새로운 클래스를 만듦
#isinstance() : 상속 관계에 따라서 객체가 어떤 클래스를 기반으로 만들었는지 확인 하는 함수 ex) str()
#어떤 클래스의 인스턴스인지 확인하기 [ isinstance() ] : isinstance(인스턴스,클래스)
class Student:
    def __init__(self):
        pass
student=Student()
print("isinstance(student,Student):",isinstance(student,Student)) #isinstance(student,Student): True
#단순한 인스턴스 확인
type(student)==Student
print(type(student)) #<class '__main__.Student'>
#isinstance() 함수와 type() 함수로 확인하는 것의 차이
class Human:
    def __init__(self):
        pass
class Student(Human):
    def __init__(self):
        pass
student=Student()
print("isinstance(student, Human):",isinstance(student,Human)) #isinstance(student, Human): True
print("type(student) == Human:",type(student)==Human) #type(student) == Human: False

#isinstance() 함수 활용
#학생 클래스를 선언
class Student:
    def study(self):
        print("공부를 합니다")
#선생님 클래스를 선언
class Teacher:
    def teach(self):
        print("학생을 가르칩니다")
#교실 내부의 객체 리스트를 생성
classroom=[Student(),Student(),Teacher(),Student(),Student()]
#반복을 적용해서 적절한 함수를 호출하게 합니다
for person in classroom:
    if isinstance(person,Student):
        person.study()
    elif isinstance(person,Teacher):
        person.teach()
