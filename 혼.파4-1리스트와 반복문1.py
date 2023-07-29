#리스트 선언/요소 접근
#[1,2,3,4] ["안","녕","하","세","요"] [273,32,103,"문자열","True","False"]
list_a=[273,53,27,"세븐틴",True,False]
print(list_a[0]) #273
print(list_a[1:4]) #[53, 27, '세븐틴']
#리스트 특정 요소 변경
list_a[0]="우지"
print(list_a) #["우지,53,27,"세븐틴",True,False]
#대괄호 안에 음수를 넣어 뒤에서 부터 요소 선택
print(list_a[-1]) #False
print(list_a[-3]) #세븐틴
#이중 사용
print(list_a[3]) #세븐틴
print(list_a[3][0]) #세
list_b=[[1,2,3],[4,5,6],[7,8,9]]
print(list_b[1]) #[4,5,6]
print(list_b[1][2]) #6
#list_c=[1,2,3] print(list_c[3]) #존재하지 않은 위치의 요소 출력시 에러 발생
#리스트 연산자
list_c=[1,2,3]
list_d=[4,5,6]
print("#리스트")
print("list_c:",list_c)  #list_c:[1,2,3]
print("list_d:",list_d)  #list_d;[4,5,6]
print("리스트 기본 연산자")
print("list_c+list_d:",list_c+list_d) #list_c+list_d:[1,2,3,4,5,6]
print("list_d*3:",list_d*3) #list_d*3:[4,5,6,4,5,6,4,5,6]
print("길이 구하기 함수")
print("len(list_c):",len(list_c)) #len(list_c):3

