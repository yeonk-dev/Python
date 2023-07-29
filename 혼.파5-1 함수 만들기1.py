#함수의 기본 def 함수 이름(): 문장
def print_3_times():
    print("안녕하세요")         #안녕하세요
    print("저는")              #저는
    print("대학생 입니다")      #대학생 입니다
print_3_times()             
#함수에 매개변수 만들기   def 함수 이름(매개변수, 매개변수... ): 문장
def print_n_times(value,n):
    for i in range(n):       #안녕
        print(value)         #안녕
print_n_times("안녕",3)      #안녕    
#매개변수 type error[1]
#def print_n_times(value,n):   #매개변수 2개를 지정했는데
#    for i in range(n):       
#        print(value)         
#print_n_times("안녕")          #하나만 넣었을 때 에러 일어남 
#TypeError: print_n_times() missing 1 required positional argument: 'n'/함수의 매개변수에 n이 없다

#매개변수 type error[2]
#def print_n_times(value,n):   #매개변수 2개를 지정했는데
#    for i in range(n):       
#        print(value)         
#print_n_times("안녕",10,30)    #3개를 넣었을 때 에러 일어남
#TypeError: print_n_times() takes 2 positional arguments but 3 were given/2개의 매개변수가 필요한데 3개가 들어왔다.
