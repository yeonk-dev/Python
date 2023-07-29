#생성자(constructor): 클래스 이름과 같은 함수
#clas  클래스 이름:
# def _ _ init _ _(self, 추가적인 매개변수):       <self> 자기 자신을 나타내는 딕셔너리
#     pass                                           ==속성/기능에 접근 할 때== self.<식별자>
class Student:
    def __init__(self,name,korean,math):
        self.name=name
        self.korean=korean
        self.math=math
Students=[
    Student("윤인성",87,98),
    Student("연하진",92,98),
    Student("구지연",76,96)
]
Students[0].name
Students[0].korean
Students[0].math  # Student 인스턴스가 생성될 때 속성이 직접 추가 됨
#소멸자(destructor) : _ _ del _ _(self)
class Test:
    def __init__(self,name):
        self.name=name
        print("{}-생성되었습니다".format(self.name))
    def __del__(self):
        print("{}- 파괴되었습니다".format(self.name))
test=Test("A")  #A-생성되었습니다
                #A- 파괴되었습니다
      
        