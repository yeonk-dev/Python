#특수한 이름의 메소드
#_ _ str _ _() 함수
class Student:
    def __init__(self,name,korean,math) :
        self.name=name
        self.korean=korean
        self.math=math
    def get_sum(self):
        return self.korean+self.math
    def get_average(self):
        return self.get_sum()/2
    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )
students=[
    Student("윤인성",89,76),
    Student("연하진",84,98),
    Student("구지연",78,98)
]
print("이름","총점","평균",sep="\t")
for student in students:
    print(str(student))
#크기 비교 함수
# eq(equal) 같다 / ne(not equal) 다르다 / gt(greater)
    