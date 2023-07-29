#튜플과 함수 : 함수의 리턴에 사용/여러 개의 값을 리턴하고 할당할 수 있음
#(1) 여러 개의 값 리턴하기
def test():
    return (10,20) 
a,b=test() #여러 개의 값 리턴
print("a=",a) #a=10
print("b=",b) #b=20
#튜플도 리스트처럼 +/*등 연산자 활용 가능 but 리스트와 별 차이 없어서 튜플로 사용하는 경우 거의 없음

#튜플을 리턴하는 함수의 예
#4장 enumerate()/items()함수를 사용하면 반복변수를 입력 하는 형식을 변형
for i,value in enumerate([1,2,3,4,5,6]):
    print("{}번째 요소는 {}입니다.".format(i,value)) #i,value 는 (i,value)형태의 튜플에서 괄호 제거
#몫/나머지를 구하는 divmod()-기본 연산자 활용
a,b=97,40
print(a//b) #2
print(a%b)  #17
#몫/나머지를 괄호 없는 튜플을 이용해 변수에 할당하고 사용
a,b=97,40
print(divmod(a,b)) #(2,17)
x,y=divmod(a,b)
print(x) #2
print(y) #17
