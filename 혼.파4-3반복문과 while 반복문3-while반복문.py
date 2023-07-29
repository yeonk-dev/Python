#while 반복문   #while 불 표현식: 문장
#while True:           #"."을 출력 #기본적으로 end가 "\n"이라 줄바꿈이 일어남
   # print(".",end="")            #빈 문자열 ""으로 바꿔서 줄바꿈이 일어나지 않게 함
#for 반복문처럼 사용
i=0                                       #0번째 반복합니다
while i<3:                                #1번째 반복합니다      
    print("{}번째 반복합니다".format(i))   #2번째 반복합니다
    i+=1 
#상태를 기반으로 반복   #remove [list]내부에 해당하는 값 하나만 제거 {while}반복문 활용시 여러 개 제거 가능
list_test=[1,2,1,2]    
value=2
while value in list_test:      #list_test 내부에 value가 있다면 반복
    list_test.remove(value)
print(list_test)  #[1, 1]
#시간을 기반으로 반복    #유닉스 타임(Unix time):세계 표준시
import time
number=0
target_tick=time.time()+5
while time.time() < target_tick:
    number+=1
print("5초 동안 {}번 반복했습니다".format(number))    #5초 동안 39391627번 반복했습니다
#break 키워드:반복문을 벗어날 때 사용
i=0
while True:
    print("{}번째 반복문입니다".format(i))
    i=i+1
    input_text=input("종료하시겠습니까(y/n):")
    if input_text in ["y","Y"]:
        print("반복을 종료합니다")
        break
#continue 키워드:현재 반복 생략, 다음 반복으로 넘어갈 때 사용
numbers=[5,15,6,20,7]
for number in numbers:
    if number<10:        #number 가 10보다 작으면 다음 반복으로 넘어감   
        continue         #15
    print(number)        #20
print(list(range(3,10/9+1,3)))


 
