# for 반복문  #for 반복자 in 반복할 수 있는 것: 코드
for i in range(100):
    print("출력")
#리스트와 함께 사용
array=[273,32,103,57,52]
for element in array:   #리스트에 반복문 적용
    print(element)
for character in "안녕하세요":
    print("-",character)  #-안 -녕 -하 -세 -요 #줄바꿈으로
#실전코딩1
numbers=[273,103,5,32,65,9,82,800]
for number in numbers:
    if number>=100:
        print("100 이상의 수:",number)
#실전 코딩2
numbers=[273,4,56,789,0]
#1
for number in numbers:
    if number%2==0:
        print("{}은 짝수입니다".format(number))
    else:
        print("{}은 홀수입니다".format(number))
for number in numbers:
    if  number%2==0:
        print(f"{number}은 짝수입니다")
    else:
        print(f"{number}은 홀수입니다")

#273는 홀수입니다
for number in numbers:
    number=str(number)
    print(number,"는",len(number),"자릿수입니다")
#273는 3 자릿수입니다
#실전 코딩3
list_of_list=[
    [1,2,3],[4,5,6,7],[8,9]
]
for list_a in list_of_list:
    for list_b in list_a:
        print(list_b)   #중첩for문
#실전 코딩4
numbers=[1,2,3,4,5,6,7,8,9]
output=[[],[],[]]
for number in numbers:
    output[(number-1)%3].append(number)
print(output)
