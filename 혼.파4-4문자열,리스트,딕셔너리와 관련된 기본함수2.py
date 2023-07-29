#현재 인덱스가 몇 번째인지 확인: enumerate()    enumerate(리스트)
#enumerate_list=["요소A","요소B","요소c"]
example_list=["승철","정한","지수"]
print("#단순 출력")                    #단순 출력
print(example_list)                   #['승철', '정한', '지수']

print("#enumerate()함수 적용 출력")     #enumerate()함수 적용 출력
print(enumerate(example_list))         #<enumerate object at 0x0000019384AF29D8>

print("#list()함수로 강제 변환 출력")    #list()함수로 강제 변환 출력
print(list(enumerate(example_list)))   #[(0, '승철'), (1, '정한'), (2, '지수')] :튜플

print("#반복문과 조합하기")                        #0번째 요소는 승철입니다       
for i,value in enumerate(example_list):           #1번째 요소는 정한입니다       
    print("{}번째 요소는 {}입니다".format(i,value)) #2번째 요소는 지수입니다
#딕셔너리와 items()함수와 반복문 조합 / 딕셔너리.items
example_dictionary={
    "과일":"사과",
    "채소":"당근"
}
print("#딕셔너리의 items() 함수")             #딕셔너리의 items() 함수
print("items():",example_dictionary.items()) #items(): dict_items([('과일', '사과'), ('채소', '당근')])

print("#딕셔너리의 items()함수와 반복문 조합하기") #딕셔너리의 items()함수와 반복문 조합하기
for key,element in example_dictionary.items():      #dictionary[과일]=사과
    print("dictionary[{}]={}".format(key,element))  #dictionary[채소]=당근
#리스트 내포
#반복문 사용한 리스트 생성
array=[]
for i in range(0,20,2):  #0,2,4,6,8,10,12,14,16,18
    array.append(i*i)  #제곱식
print(array)
#리스트 안에 for문 사용  : list=[표현식 for 반복자 in 반복할 수 있는 것]
array=[i*i for i in range(0,20,2)]  #최종 결과를 앞에 작성 i*i
print(array)
#조건을 활용한 리스트내포 :list=[표현식 for 반복자 in 반복할 수 있는 것 if 조건문]
array=["우지","승철","정한","백현"]
output=[sep for sep in array if sep !="백현"]
#array의 요소를 sep이라고 할 때 백현이 아닌 sep으로 리스트를 재조합 해주세요
print(output)

