#dict_key={
    #name:"딸기라떼", #name error
   # type:"음료"      #name 이라는 이름을 변수로 만들기
#}
#print(dict_key)

name="이름"
dict_key={
    name:"딸기라떼",
    type:"음료"
}
print(dict_key)  #{'이름': '딸기라떼', <class 'type'>: '음료'}

dictionary={
    "name":"딸기라떼",
    "type":"음료",
    "ingredient":["딸기","연유","설탕"]
}
#딕셔너리에 값 추가/제거
dictionary["price"]=5000
print(dictionary)    #값 추가
dictionary["name"]="딸기연유라떼"
print(dictionary) #기본의 값 새로운 값으로 대치
del dictionary["type"]
print(dictionary)       #특정 키 요소 제거
