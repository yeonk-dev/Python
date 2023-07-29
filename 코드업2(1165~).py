#코드업1165번 축구의 신 1
# cur_time, our_score = map(int, input().split())
# for i in range(cur_time, 90, 5):
#     our_score = our_score+1
# print(our_score)

#코드업1166 : 윤년 판별
#(1) 400의 배수이면 무조건 윤년이다.
#(2) (1)이 아닌 수 중에 4의 배수이며, 100의 배수가 아니면 윤년이다.
# year=int(input())
# if year%400==0:
#     print("leap")
# elif  year%4==0 and year%100!=0:
#     print("leap")
# else:
#     print("Normal")

#코드업 1167 : 두 번째 수
# data = list(map(int, input().split()))
# data.sort()
# print(data[1])

#1071 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기1(설명) 반복문
# i=input().split()
# for x in i:
#     if int(x)==0:
#       break
#     else:
#        print(x)
#Codeup 1170 - 당신의 학번은 1
grade, group, number = input().split()
number = int(number)

if(number < 10):
    number = '0' + str(number)

print(grade + group + str(number))
#1171: 당신의 학번은 2

