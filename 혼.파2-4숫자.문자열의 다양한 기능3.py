#대소문자 바꾸기
#upper
a="hello python programming...!"
print(a.upper())
#lower
a="hello python programming...!"
print(a.lower())
#문자열 양옆의 공백 제거하기
#strip():문자열 양옆 공백 제거
#lstrip():문자열 왼쪽의 공백 제거
#rstrip():문자열 오른쪽의 공백 제거
input_a="""
       안녕하세요
문자열의 함수를 알아봅시다  #의도하지 않은 줄바꿈 들어감
"""
print(input_a)
print(input_a.strip())
#문자열 찾기
#find 왼쪽부터 찾아서 처음 등장하는 위치 찾기
#rfind 오른쪽 부터 찾아서 처음 등장하는 위치 찾기
output_a="오렌지오렌지포도".find("오렌지") #0
print(output_a)
output_b="오렌지오렌지바나나".rfind("오렌지") #3
print(output_b)
#문자열 내부에 있는 문자열 확인 "in" 연산자
print("안녕"in"안녕하십니까") #true
print("잘자"in"안녕하십니까") #false
#문자열 자르기 split
a="10 20 30 40 50".split()
print(a) #['10','20','30','40','50'] #리스트(list)
#실전코드실행1
a=input("> 1번째 숫자:") 
b=input("> 2번째 숫자: ")
print()
print("{}+{}={}".format(a,b,int(a)+int(b)))
#실전코드실행2
string="hello"
string.upper()
print("A지점:",string)  #대문자로 출력 안됨
print("B지점:",string.upper()) #대문자로 출력


