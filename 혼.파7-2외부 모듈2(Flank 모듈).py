#Flask모듈 : 작은 기능만을 제공하는 웹 개발 프레임워크
#Django :다양한 기능을 제공하는 웹 개발 프레임워크
#pip install flask (공식 홈페이지: http://flask.pocoo.org)

#flask 모듈 사용하기
from flask import Flask
app=Flask(__name__)
@app.route("/") #데코레이터(decorator)
def hello():
    return "<h1>Hello World</h1>"
#set FLASK_APP=파일 이름.py  <리눅스 or 맥>  export FLASK_APP=파일 이름.py
#flask run                                  flask run

#beautifulsoup 스크레이핑 실행하기
#모듈을 읽어들입니다
from flask import Flask
from urllib import request
from bs4 import BeautifulSoup
#웹 서버를 생성합니다
app=Flask(__name__)
@app.route("/")
def hello():
    #urlopen()함수로 기상청의 전국 날씨를 읽습니다
    target=request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
    #beautifulsoup를 사용해 웹 페이지를 분석합니다.
    soup=BeautifulSoup(target,"html.parser")
    #location태그를 찾습니다
    output=""
    for location in soup.select("location"):
        output+="<h3>{}</h3>".format(location.select_one("city").string)
        output+="날씨:{}<br/>".format(location.select_one("wf").string)
        output+="최저/최고 기온: {}/{}"\
            .format(\
                location.select_one("tmn").string,\
                location.select_one("tmx").string\
                )
        output+="<hr/>"
    return output