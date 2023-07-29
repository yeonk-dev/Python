#가비지 컬렉터(garbage collector)
#스왑(swap):메모리가 부족해 지면 하드디스크를 메모리처럼 사용해 무언가를 올리기 시작함
#메모리가 가득 차는 것을 방지하기 위해 "더 이상 사용할 가능성이 없는 데이터를 메모리에서 제거!!"
#"더 이상 사용할 가능성이 없는 데이터":변수에 저장되지 않거나,함수 등에서 나오면서 변수를 활용할 수 없게 되는 경우

#가비지 컬렉터:변수가 저장하지 않는 경우
class Test:
    def __init__(self,name):
        self.name=name
        print("{}-생성되었습니다".format(self.name))  #A-생성되었습니다
    def __del__(self):                               #A-파괴되었습니다
        print("{}-파괴되었습니다".format(self.name))  #B-생성되었습니다
Test("A")                                            #B-파괴되었습니다
Test("B")                                            #C-생성되었습니다
Test("C")                                            #C-파괴되었습니다
#가비지 컬렉터:변수에 저장한 경우
class Test:
    def __init__(self,name):
        self.name=name
        print("{}-생성되었습니다".format(self.name))  #A-생성되었습니다
    def __del__(self):                               #B-생성되었습니다                      
        print("{}-파괴되었습니다".format(self.name))  #C-생성되었습니다
a=Test("A")                                          #A-파괴되었습니다
b=Test("B")                                          #B-파괴되었습니다
c=Test("C")                                          #C-파괴되었습니다

