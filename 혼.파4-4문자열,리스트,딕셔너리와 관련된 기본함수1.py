#리스트에 적용할 수 있는 기본 함수:min(),max(),sum()
#리스트 뒤집기: reserved()
#현재 인덱스가 몇 번째인지 확인: enumerate()
#딕셔너리로 쉽게 반복문 작성:items()
#리스트 안에 for문 사용: 리스트 내포

#리스트에 적용할 수 있는 기본 함수:min() 최솟값 ,max() 최댓값 ,sum() 내부에 값 모두 더함
numbers=[103,52,273,32,77]
print(min(numbers)) #32
print(max(numbers)) #273
print(sum(numbers)) #537
#리스트 사용 하지 않고 함수 적용
print(min(103,52,3)) #3
print(max(120,37,89)) #120
#리스트 뒤집기: reserved()
list_a=[1,2,3,4,5]
list_reversed=reversed(list_a)
print("reversed([1,2,3,4,5]):", list_reversed) #reversed([1,2,3,4,5]): <list_reverseiterator object at 0x00000204B9C852B0>
print("list(reversed([1,2,3,4,5])):",list(list_reversed)) #list(reversed([1,2,3,4,5])): [5, 4, 3, 2, 1]

print("# reversed() 함수와 반복문") # reversed() 함수와 반복문
print("for i in reversed([1,2,3,4,5]):")  #for i in reversed([1,2,3,4,5]):
for i in reversed(list_a):           
    print("-",i)                    # -5 -4 -3 -2 -1 (줄 바꿔서 차례로 출력)
#
temp=reversed([1,2,3,4,5])
for i in temp:                          #코드 실핵시 첫 번째 반복문 부분만 실행
    print("첫 번째 반복문:{}".format(i))
for j in temp:                          #because  reversed()는 제너레이터                       
    print("두 번째 반복문: {}".format(j))
#
numbers=[1,2,3,4,5]
for i in reversed(numbers):               #reversed() 함수와 반복문을 조합할 때는 for 구문 내부에 바로 넣음
    print("첫 번째 반복문:{}".format(i))
for i in reversed(numbers):
    print("두 번째 반복문: {}".format(i))
#확장 슬라이싱
j=[1,2,3]
print(j[::-1]) #[3, 2, 1]
print("세븐틴입니다"[::-1])   #다니입틴븐세
