#try except 구문 #try: 예외가 발생할 가능성이 있는 코드 except:예외가 발생했을 때 실행할 코드
try:
    number_input_a=int(input("숫자 입력="))
    print("원의 반지름=",number_input_a)
    print("원의 넓이=",3.14*number_input_a**2)
except:
    print("무언가 잘못되었습니다") #yes! 입력 시 "무언가 잘못되었습니다" 출력.예외 처리하고 정상적으로 종료
#try except 구문과 pass 키워드 조합하기: try:예외가 발생할수 있는 코드 except: pass
list_input_a=["52","273","32","스파이","103"]
list_number=[]
for item in list_input_a:
    #숫자로 변환하여 리스트에 추가
    try:
        float(item)  #예외가 발생하면 알아서 다음으로 진행 안됨
        list_number.append(item) #예외 없이 통과했으면 리스트에 in
    except:
        pass
print("{}내부에 있는 숫자는".format(list_input_a)) #['52', '273', '32', '스파이', '103']내부에 있는 숫자는
print("{}입니다".format(list_number)) #['52', '273', '32', '103']입니다 /if구문보다 아주 약간 속도가 느림
#try except else 구문
#try:예외가 발생할 가능성이 있는 코드  except:예외가 발생하지 않았을 때 실행할 코드
#else: 예외가 발생하지 않았을 때 실행할 코드
try:
    number_input_a=int(input("정수 입력="))
except:
    print("정수를 입력하지 않았습니다")
else:
    print("원의 반지름=",number_input_a)
    print("원의 넓이=",3.14*number_input_a**2)
    
