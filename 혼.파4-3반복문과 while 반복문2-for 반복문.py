#for 반복문    # for 숫자 변수 in 범위:
              #      코드
#범위와 함께 사용
for i in range(5):                  #0=반복 변수
     print(str(i)+"=반복 변수")      #1=반복 변수
print()                             #2=반복 변수
                                    #3=반복 변수
                                    #4=반복 변수
for i in range(6,10):
    print(str(i)+"=반복변수")
print()
for i in range(1,10,2):             #range(a,b,c)  a부터 c씩 증가하면서 b-1까지의 정수로 범위 출력
    print(str(i)+"=반복변수")
print()
#리스트와 범위 조합하기
array=[273,56,7,89,10]    #273 56 7 89 10 줄바꿈해서 각자 출력(리스트 형태를 벗어남)
for element in array:
    print(element)
for i in range(len(array)):                    
    print("{}번째 반복:{}".format(i,array[i]))  #0번째 반복:273 ---4번째 반복:10 까지 줄바꿈 해서 연속 출력
#반대로 반복하기
for i in range(2,0-1,-1):                  #현재 반복 변수:2
    print("현재 반복 변수:{}".format(i))    #현재 반복 변수:1
                                           #현재 반복 변수:0
#반대로 반복하기(2) reversed()              #현재 반복 변수:2    
for i in reversed(range(3)):               #현재 반복 변수:1
    print("현재 반복 변수:{}".format(i))    #현재 반복 변수:0
    