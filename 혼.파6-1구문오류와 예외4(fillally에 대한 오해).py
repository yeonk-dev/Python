#finally 함수 자세히 알아보기
#closed 속성: 파일을 제대로 닫았는지 알 수 있음
#파일이 제대로 닫혔는지 확인하기(try except 구문 사용)
try:
    file=open("info.txt","w") 
    #여러가지 처리를 수행합니다
    file.close() #파일을 닫습니다
except Exception as e:
    print(e)
print("파일이 제대로 닫혔는지 확인하기") #데몬(daemon)/서비스(service).항상 켜져있는 프로그램은 문제가 생길 수 있음
print("file.closed:",file.closed) #file.closed: True
#파일 처리 중간에 예외 발생(try except 구문 사용)
try:
    file=open("info.txt","w")
    예외.발생해라()         
    file.close()
except Exception as e:
    print(e)                     #name '예외' is not defined
print("파일이 제대로 닫혔는지 확인하기")
print("file.closed:",file.closed) #file.closed: False
#중간에 예외가 발생해서 try구문 중간에 튕기면 파일이 안 닫힘 =반드시 finally구분을 사용하여 파일을 닫아야 함

#finally 구문 사용해 파일 닫기
try:
    file(open("info.txt","w"))
    예외.발생해라()
except Exception as e:
    print(e)
finally:
    file.close()
print("파일이 제대로 닫혔는지 확인하기")
print("file.closed:",file.closed) #file.closed: True

# try except 구문 끝난 후 파일 닫기
try:
    file=open("info.txt","w")
    예외.발생해라()
except Exception as e:
    print(e)          #name '예외' is not defined
file.close()
print("파일이 제대로 닫혔는지 확인하기")
print("file.closed:",file.closed) #file.closed: True