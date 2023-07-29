dictionary={}
print("요소 추가 이전:",dictionary)
dictionary["name"]="대학생"
dictionary["head"]="전공"
dictionary["body"]="헬스"
print("요소 추가 후:",dictionary)

#요소 제거
del dictionary["name"]
del dictionary["body"]
del dictionary["head"]
print("요소 제거 이후:",dictionary)
#dictionary["key"]  #key error  존재하지 않는 키에 접근 할때 발생
#딕셔너리 내부에 키가 있는지 확인
dictionary={
    "name":"장연경",
    "type":"돼지",
    "ingredient":["탄수화물","단백질"],
    "origine":"대한민국"
}
#in 키워드
key= input("type:")
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다")
#get() 함수
value=dictionary.get("type")
print("값:",value)    #존재하는 키 접근시 값:돼지 형식으로 나옴
value=dictionary.get("kind")
print("값",value)     #존재하지 않는 키 접근시  값:None
if value==None:
    print("존재하지 않은 키에 접근 하였습니다")   #존재하지 않은 키에 접근하였습니다
#for 반복문: 딕셔너리와 함께 사용
for key in dictionary:               #name : 장연경
     print(key,":",dictionary[key])  #type : 돼지
                                    #ingredient : ['탄수화물', '단백질']
                                    #origine : 대한민국
