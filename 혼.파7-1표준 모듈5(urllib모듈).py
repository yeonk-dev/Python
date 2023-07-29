#urlib 모듈 (URL[Uniform resource locator]을 다루는 라이브러리)
#웹브라우저의 주소창에 입력하는 주소 - 인터넷 주소를 활용할 때 사용하는 라이브러리
#from urllib import request
#urlopen() 함수로 구글의 메인 페이지를 읽음
#target =request.urlopen("http://google.com")
#output=target.read()
#print(output)
#urlopen() 함수: URL주소의 페이지를 열어주는 함수
#b=바이너리 데이터(binary data)

#실전코딩1(p.330-331)
#현재 디렉토리를 읽어들이고 파일인지 디렉터리인지 구분하기
#os.listdir() / os.path.isdir() 함수 사용 - 특정 디렉터리를 읽어 파일 디렉터리인지 구분
import os
output=os.listdir(".")
print("os.listdir():",output)
print()
print("# 폴더와 파일 구분하기")
for path in output:
    if os.path.isdir(path):
        print("폴더:",path)
    else:
        print("파일:",path)
#폴더라면 또 탐색하기:재귀구성으로 폴더 내부에 있는 모든 파일 탐색
print("#폴더라면 또 탐색하기")
import os
def read_folder(path):
    #폴더의 요소 읽어들이기
    output=os.listdir(path)
#폴더의 요소 구분하기
for item in output:
    if os.path.isdir(item):
        #폴더라면 계속 읽어들이기
        read_folder(item)
    else:
        #파일이라면 출력하기
        print("파일:",item)
#현재 폴더의 파일/폴더를 출력합니다
read_folder(".")

