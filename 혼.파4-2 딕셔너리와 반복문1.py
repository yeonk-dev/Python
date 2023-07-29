#리스트/인덱스를 기반으로 값을 저장 변수=[] :딕셔너리/키를 기반으로 값을 저장 변수={}
#"키A":10 (문자열을 키로 사용) , 1:  40(숫자를 키로 사용), False: 50 (불을 키로 사용)
#딕셔너리 선언하기
dict_a={
    "name": "극한직업",
    "type": "코미디 무비"
     }
#딕셔너리 요소 접근
print(dict_a)  #{'name':'극한직업','type':'코미디 무비'}
print(dict_a["name"]) #극한직업
print(dict_a["type"]) #코미디무비
#리스트와 딕셔너리를 값으로 넣기
dict_b={
    "director":["김지철 감독","강주연 연출"],
    "cast":["이하늬","류승룡","공명"]
}
print(dict_b)   #{'director':['김지철 감독','강주연 연출'],'cast':['이하늬','류승룡','공명']}
print(dict_b["director"]) #['김지철 감독','강주연 연출']
#딕셔너리 연습 코딩
dictionary={
    "name":"딸기라떼",
    "type":"음료",
    "ingredient":["딸기","연유","설탕"]
}
print("name:",dictionary["name"])
print("type:",dictionary["type"])
print("ingredient:",dictionary["ingredient"])

dictionary["name"]="딸기 연유 라떼"
print("name:",dictionary["name"]) #값 변경
print(dictionary["ingredient"][1]) #특정 값 출력 #연유
