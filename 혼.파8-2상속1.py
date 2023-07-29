#상속(inheritance): 다른 누군가가 만들어 놓은 기본 형태에 내가 원하는 것만 교체하는 것
#다중 상속 : 다른 누군가가 만들어 놓은 형태들을 조립하여 내가 원하는 것만 교체하는 것
#부모(parent): 프로그래밍 언어에서 기반이 되는 것 자식(child):이를 기반으로 생성한 것
#상속의 활용
#부모 클래스를 선언
class Parent:
    def __init__(self):
        self.value="테스트"
        print("Parent 클래스의 __init()__ 메소드가 호출되었습니다")
    def test(self):
        print("Parent 클래스의 test() 메소드입니다")
#자식 클래스를 선언
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child 클래스의 __init()__ 메소드가 호출되었습니다.")
#자식 클래스의 인스턴스를 생성하고 부모의 메소드를 호출
child=Child()      #Parent 클래스의 __init()__ 메소드가 호출되었습니다
child.test()       #Child 클래스의 __init()__ 메소드가 호출되었습니다.
print(child.value) #Parent 클래스의 test() 메소드입니다
                   #테스트