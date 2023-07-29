#try 구문 내부에서 return 키워드를 사용하는 경우
def test():
    print("test() 함수의 첫 줄입니다.") #출력
    try:
        print("try 구문이 실행되었습니다") #출력
        return
        print("try 구문의 return 키워드 뒤 입니다")
    except:
        print("except 구문이 실행되었습니다")
    else:
        print("else 구문이 실행되었습니다")
    finally:
        print("finally 구문이 실행되었습니다") #출력
    print("test()함수의 마지막 줄입니다")
test()                                                   #test() 함수의 첫 줄입니다.
#try구문 중간에서 탈출해도 finally구문은 무조건 실행        #try 구문이 실행되었습니다
#try구문에서 원할 때 return키워드로 빠져나가도 무조건 닫힘   #finally 구문이 실행되었습니다

#finally 키워드 활용
def write_test_file(filename,text):
    try:
        file=(open(filename,"w"))
        return
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        file.close()
write_test_file("test.txt","안녕하세요!")
#반복문과 함께 사용하는 경우
print("프로그램이 시작되었습니다")
while True:
    try:
        print("try 구문이 실행되었습니다")
        break
        print("try 구문의 break 키워드 뒤 입니다")
    except:
        print("except 구문이 실행되었습니다")
    finally:
        print("finally 구문이 실행되었습니다")
    print("while반복문의 마지막 줄입니다")

print("프로그램이 종료되었습니다")
#프로그램이 시작되었습니다
#try 구문이 실행되었습니다
#finally 구문이 실행되었습니다
#프로그램이 종료되었습니다    / 코드 실행시 break 키워드로 try 구문 전체를 빠져나가도 finally  구문 실행