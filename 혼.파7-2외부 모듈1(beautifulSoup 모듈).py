#beautifulSoup 모듈 (공식 문서 홈피: http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
#beautifulSoup 모듈로 날씨 가져오기
from urllib import request #모듈을 읽어 들입니다
from bs4 import BeautifulSoup
#urlopen() 함수로 기상청의 전국 날씨를 읽습니다
target=request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
#BeautifulSoup을 사용해 웹 페이지를 분석합니다
soup=BeautifulSoup(target,"html.parser")
#location 태그를 찾습니다
for location in soup.select("location"):
    print("도시:",location.select_one("city").string)
    print("날씨:",location.select_one("wf").string)
    print("최저기온:",location.select_one("tmn").string)
    print("최고기온:",location.select_one("tmx").string)
