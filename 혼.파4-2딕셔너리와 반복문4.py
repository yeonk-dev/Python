#실전코딩1 p.171
pets=[
    {"name":"구름","age":5},
    {"name":"초코","age":3},
    {"name":"아지","age":1},
    {"name":"호랑이","age":1}
]
print("우리 동네 애완 동물들")
for pet in pets:
    print(pet["name"],str(pet["age"])+"살") #숫자와 문자열 사이에 빈칸 없게 출력
#for pet in pets:
    #print("{} {}살".format(pet["name"],str(pet["age"])))   #format 함수 사용문
#실전코딩2 p.172
numbers=[1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter={}
for number in numbers:
    if number in counter:
        counter[number]+=1
    else:
        counter[number]=1
print(counter)           #실행결과 {1: 3, 2: 4, 6: 1, 8: 2, 4: 3, 3: 3, 9: 3, 5: 2, 7: 2}
#실전코딩3 p.173
character={
    "name":"기사",
    "level":12,
    "items":{
        "sword":"불꽃의 검",
        "amor":"풀플레이트"
    },
    "skill":["베기","세게 베기","베기아주 세게 베기"]
}
for key in character: 
    if type(character[key]) is list:
        for k in character[key]:
            print("{} : {}".format(key, k))
    elif type(character[key]) is dict:
        for j in character[key]:
            print("{} : {}".format(j, character[key][j]))
    else:
        print("{} : {}".format(key, character[key]))
print(character["skill"])
print(character["items"])


