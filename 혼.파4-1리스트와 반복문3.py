#리스트에서 요소 제거하기
#인덱스로 제거하기:del 리스트명[인덱스]/리스트명.pop(인덱스)
list_a=[0,1,2,3,4,5]
print("#리스트의 요소 하나 제거하기")
#제거방법:del
del list_a[1]
print("del list_a[1]:",list_a) #del list_a[1]:[0,2,3,4,5]
#제거방법:pop()
list_a.pop(3)
print("pop(3):",list_a) #[0,2,3,5] 
#매개변수에 아무 것도 입력하지 않으면 자동으로 -1이 들어가는 것으로 취급해서 마지막 요소 제거
list_a.pop()
print("pop():",list_a) #[0,2,3]
#범위를 지정해 리스트의 요소 한꺼번에 제거
list_b=[1,2,3,4,5,6,7]
del list_b[3:6]
print(list_b) #[1,2,3,7]
#지정한 위치를 기준으로 한쪽 전부 제거
list_c=[0,1,2,3,4,5,6]
del list_c[:3] #3을 기준(3번째 불포함 왼쪽 모두 제거)
print(list_c) #[3,4,5,6]
list_d=[0,1,2,3,4,5,6]
del list_d[3:] #3을 기준(3번째 포함 오른쪽 모두 제거)
print(list_d) #[0,1,2]
#값으로 제거하기:remove :리스트.remove(값)
list_e=[1,2,1,2]
list_e.remove(2) 
print(list_e) #[1,1,2]
#모두 제거하기:clear :리스트.clear()
list_f=[1,2,3,4,5,6]
list_f.clear()
print(list_f) #[] 값 모두 제거
#리스트 내부에 있는지 확인하기 :in/not in
list_g=[245,84,12,9,435]
print(245 in list_g) #True
print(1 in list_g)   #False
print(78 not in list_g) #True
print(9 not in list_g)  #False
