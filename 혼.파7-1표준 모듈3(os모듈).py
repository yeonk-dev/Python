#os모듈 :운영체제와 관련된 기능/ 새로운 폴더 만들기 or 폴더 내부의 파일 목록을 보는 것
import os #모듈을 읽어 오기
print("현재 운영체제:",os.name) #기본 정보 몇 개 출력
print("현재 폴더:",os.getcwd)
print("현재 폴더 내부의 요소:",os.listdir())
#폴더를 만들고 제거(폴더가 비어있을 때만 제거 가능)
os.mkdir("hello")
os.rmdir("hello")
#파일을 생성하고 +파일 이름을 변경합니다
with open("original.txt","w") as file:
    file.write("hello")
os.rename("original.txt","new.txt")
#파일을 제거합니다
os.remove("new.txt")
#os.unlink("new.txt")
#시스템 명령어 실행
os.system("dir")

#os.remove()=os.unlink() 서로 같은 함수!

#os.system("rm -rf/") 리눅스에서 입력시 루트 권한이 있을 경우 컴퓨터의 모든 것 삭제