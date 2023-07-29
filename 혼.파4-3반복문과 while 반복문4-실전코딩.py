#실전코딩1 p.188 2번
key_list=["name","hp","mp","level"]
value_list=["기사",200,30,5]
character={}
for i in range(0,len(key_list)):
    character[key_list[i]]=value_list[i]
print(character)        #{'name': '기사', 'hp': 200, 'mp': 30, 'level': 5}
#실전코딩2 p.188 3번
limit=10000
i=1
sum_value=0
while sum_value<limit:
    sum_value+=i
    i+=1                      
print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다".format(i,limit,sum_value))
#실전코딩3 p.189 4번
max_value=0
a=0
b=0
for i in range(1,100//2+1):
    j=100-i
    answer=i*j
    if max_value<answer:
        a=i
        b=j
        max_value=answer
print("최대가 되는 경우: {}*{}={}".format(a,b,max_value))
print(f"최대가 되는 경우: {a}*{b}={max_value}")