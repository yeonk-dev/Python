#라이브러리(library):정상적인 제어를 하는 모듈 :개발자가 모듈의 기능을 호출하는 형태
from math import sin,cos,tan,floor,ceil
print("sin(1)=",sin(1))
print("cos(1)=",cos(1))
print("tan(1)=",tan(1))
print("floor(2.5):",floor(2.5))
print("ceil(2.5):",ceil(2.5))
#프레임워크(framework):제어 역전이 발생하는 모듈 :모듈이 개발자가 작성한 코드를 실행하는 형태
from flask import Flask
app=Flask(__name__)
@app.route("/") 
def hello():
    return "<h1>Hello World</h1>"
    
#제어 역전(Ioc:Inverse of control) 의 여부로 라이브러리와 프레임워크 구분
