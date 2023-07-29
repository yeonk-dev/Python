# @classmethod : 데코레이터(decorator)
#클래스 함수 만들기
#class 클래스 이름:                                  #클래스 함수 호출
#    @classmethod                                     =클래스 이름.함수 이름(매개변수)
#    def 클래스 함수(cls,매개변수): #cls=class(클래스)
#        pass
class Student:
    #클래스 변수
    count=0
    students=[]
    #클래스 함수
    @classmethod
    def print(cls):
        print("-------학생 목록--------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("-------- ------- -------")
    # 인스턴스 함수 
    def __init__(self,name,korean,math):
        self.name=name
        self.korean=korean
        self.math=math
        Student.count+=1
        Student.students.append(self)
    
    def get_sum(self):
        return self.korean+self.math
    
    def get_average(self):
        return self.get_sum()/2
    
    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average())

#학생 리스트를 선언
Student("윤인성",87,98)
Student("연하진",92,98)
Student("구지연",76,86)
#현재 생성된 학생을 모두 출력
Student.print()