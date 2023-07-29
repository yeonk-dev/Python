#리스트에 요소 추가 리스트명.append(요소)/리스트명.insert(위치,요소)
#리스트에 요소 추가
list_a=[1,2,3]
print("#리스트뒤에 요소 추가")
list_a.append(4)
list_a.append(5)
print(list_a)  #{1,2,3,4,5}
print("#리스트 중간에 요소 추가")
list_a.insert(0,10)  #[10,1,2,3,4,5]
print(list_a)
#extend 한 번에 여러 요소 추가
list_a.extend([8,9,10])
print(list_a) #[10,1,2,3,4,5,8,9,10]
#리스트연결 연산자와 요소 추가의 차이
list_b=[1,2,3]
list_c=[4,5,6]
print(list_b+list_c) #[1,2,3,4,5,6]
print(list_b)  #[1,2,3]
print(list_c)  #[4,5,6]#list_a 와 list_b에는 변화 없음(비파괴적 처리)

list_b.extend(list_c)
print(list_b)   #[1,2,3,4,5,6] #list_b에 직접적인 변화 일어남(파괴적 처리)
print(list_c)  #[4,5,6]
