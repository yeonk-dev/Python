#크기 비교 함수
# eq(equal) 같다 / ne(not equal) 다르다 / gt(greater) /ge(greater than or equal) 크거나 같다
# lt(less than) 작다 / le (less than or equal) 작거나 같다
class Student:
    def __init__(self,name,korean,math):
        self.name=name
        self.korean=korean
        self.math=math
    def get_sum(self):
        return self.korean+self.math
    def get_average(self):
        return self.get_sum()/2
    def __str__(self):
        "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )
    def __eq__(self, value):
        return self.get_sum()==value.get_sum()
    def __ne__(self,value):
        return self.get_sum() !=value.get_sum()
    def __gt__(self,value):
        return self.get_sum()>value.get_sum()
    def __ge__(self,value):
        return self.get_sum()>=value.get_sum()
    def __lt__(self,value):
        return self.get_sum()<value.get_sum()
    def __le__(self,value):
        return self.get_sum() <= value.get_sum()
#학생 리스트를 선언
students=[
    Student("윤인성",85,93),
    Student("연하진",59,93),
    Student("구지연",96,94)
]
#학생을 선언
student_a=Student("윤인성",85,93)
student_b=Student("연하진",59,93)

print("student_a==student_b=",student_a==student_b) #student_a==student_b= False
print("student_a !=student_b=",student_a!=student_b) #student_a !=student_b= True
print("student_a>student_b=",student_a>student_b)    #student_a>student_b= True
print("student_a>=student_b=",student_a>=student_b) #student_a>=student_b= True
print("student_a<student_b=",student_a<student_b)  #student_a<student_b= False
print("student_a<=student_b=",student_a<=student_b) #student_a<=student_b= False

#예외처리(typeerror)
class Student:
    def __eq__(self,value):
        if not isinstance(value,Student):
            raise TypeError("Student 클래스의 인스턴스만 비교할 수 있습니다")
        return self.get_sum()==value.get_sum()
    #생략
students=[
    Student("윤인성",85,93),
    Student("연하진",59,93)
    ]    
student_c=Student("윤인성",85,93)
print(student_c==10)
#TypeError: Student 클래스의 인스턴스만 비교할 수 있습니다.
