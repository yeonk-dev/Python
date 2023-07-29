#람다(lamda): 함수라는"기능"을 매개변수로 전달하는 코드 많이 사용/이를 더 효율적으로 작성하기 위해 사용
#함수의 매개변수로 함수 전달하기
def call_10_times(func): #매개변수로 받은 함수를 10번 호출하는 함수
    for i in range(10):
        func()
def print_hello():  #간단한 출력
    print("안녕하세요")
call_10_times(print_hello) #조합
#filter()함수와 map()함수 :★함수를 매개변수로 전달하는 대표적인 표준(내장)함수★
#map(함수,리스트):리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 구성하는 함수
#filter(함수,리스트):리스트의 요소를 함수에 넣고 ※리턴된 값이 True인 것※으로, 새로운 리스트를 구성해주는 함수
def power(item):
    return item*item
def under_3(item):
    return item<3
list_input_a=[1,2,3,4,5]
#map() 함수 사용
output_a=map(power,list_input_a)
print("#map()함수의 실행결과")                    #map()함수의 실행결과
print("map(power,list_input_a):",output_a)#제너레이터/map(power,list_input_a): <map object at 0x000001CAC1AC4EF0>
print("map(power,list_input_a):",list(output_a)) #map(power,list_input_a): [1, 4, 9, 16, 25]
#filter() 함수 사용
output_b=filter(under_3,list_input_a)
print("#filter()함수의 실행결과")                     #filter()함수의 실행결과
print("filter(under_3,list_input_a):",output_b)#제너레이터/filter(under_3,list_input_a): <filter object at 0x000001CAC1BAD160>
print("filter(under_3,list_input_a):",list(output_b))#filter(under_3,list_input_a): [1, 2]

#람다(lamda):간단한 함수를 쉽게 선언하는 방법/lamda 매개변수:리턴값
power=lambda x:x*x
under_3=lambda x:x<3
list_input_a=[1,2,3,4,5]
#map() 함수 사용
output_a=map(power,list_input_a)
print("#map()함수의 실행결과")                    
print("map(power,list_input_a):",output_a)#제너레이터/map(power,list_input_a): <map object at 0x000001CAC1AC4EF0>
print("map(power,list_input_a):",list(output_a))#map(power,list_input_a): [1, 4, 9, 16, 25]
#filter() 함수 사용
output_b=filter(under_3,list_input_a)
print("#filter()함수의 실행결과")                     
print("filter(under_3,list_input_a):",output_b)#제너레이터/filter(under_3,list_input_a): <filter object at 0x000001CAC1BAD160>
print("filter(under_3,list_input_a):",list(output_b))#filter(under_3,list_input_a): [1, 2]
#인라인 람다
list_input_a=[1,2,3,4,5]
output_a=map(lambda x:x*x,list_input_a)
print("#map()함수의 실행결과")                    
print("map(power,list_input_a):",output_a)#제너레이터/map(power,list_input_a): <map object at 0x000001CAC1AC4EF0>
print("map(power,list_input_a):",list(output_a))#map(power,list_input_a): [1, 4, 9, 16, 25]
#filter() 함수 사용
output_b=filter(lambda x:x<3,list_input_a)
print("#filter()함수의 실행결과")                     
print("filter(under_3,list_input_a):",output_b)#제너레이터/filter(under_3,list_input_a): <filter object at 0x000001CAC1BAD160>
print("filter(under_3,list_input_a):",list(output_b))#filter(under_3,list_input_a): [1, 2]

#매개변수가 여러 개인 람다
lambda x,y:x*y

