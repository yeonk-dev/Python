#코드에 이름 붙이기(가독성이 좋은 코드 만들기)
#설명이 없는 코드
number_input_a=input("숫자입력=")
radius=float(number_input_a)
print(2*3.14*radius)
print(3.14*radius*radius) # 원의 둘레와 넓이를 구한다고 생각하기에 시간이 걸임
#주석이 있는 코드
number_input_a=input("숫자입력=")
radius=float(number_input_a)
print("원의 둘레:",2*3.14*radius)  #주석이 있는 코드
print("원의 넓이:",3.14*radius*radius)
#코드에 의미있는 이름을 붙이는 코드(가독성이 좋은 코드)
def number_input():
    output=input("숫자입력=")
    return float(output)
def get_circumference(radius):
    return 2*3.14*radius
def get_circle_area(radius):
    return 3.14*radius*radius
radius=number_input()
print(get_circumference(radius))   #코드가 길어졌지만 
print(get_circle_area(radius))     #코드 본문만 봐도 주석없이 무엇을 하는 코드 인지 알수 있음(모듈module)
#코드 유지보수
#3.14를 숫자를 입력한 상태
def get_circumference(radius):
    return 2*3.14*radius
def ger_circle_area(radius):
    return 3.14*radius*radius
#3.14를 pi라는 변수로 설정한 상태(가독성 높이는 방법)
pi=3.14
def get_circumference(radius):
    return 2*pi*radius
def get_circle_area(radius):
    return pi*radius*radius
print(ger_circle_area(radius))
#선언할 변수를 바꾸고 싶을 때(임의로 수정할 경우 실수 발생 가능)
#함수를 사용하지 않는 경우
print("<p>{}</p>",format("안녕하세요")) #<p>{}</p> 안녕하세요
print("<p>{}</p>".format("간단한 html 태그를 만드는 예 입니다")) #<p>간단한 html 태그를 만드는 예 입니다</p>
#'단순한<p></p>'로 감싸지 말고 "<p class'content-line'></p>"로 감싸주세요 요청
def p(content):
    #기존 코드 주석 처리
    #return "<p>{}</p>".format(content)
    #2017.08.15 요청 반영
    return "<p class='content-line'>{}</p>".format(content)
print(p("안녕하세요")) #<p class='content-line'>안녕하세요</p>
print(p("간단한 HTML 태그를 만드는 예입니다.")) #<p class='content-line'>간단한 HTML 태그를 만드는 예입니다.</p>
