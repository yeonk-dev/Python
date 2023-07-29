#실습 : person 딕셔너리의 생성과 조회
person={'이름' : '홍길동', '나이' :26, '몸무게':82}
print(person['이름']) #홍길동
print(person['나이']) #26
print(person['몸무게']) #82
#실습 : students 딕셔너리의 생성과 조회
students= {2019001:'이순신',2019002:'김유신',2019003:'강감찬'}
print(students[2019001]) #이순신
print(students[2019002]) #김유신
print(students[2019003]) #강감찬
#lab 6-1 :딕셔너리와 생성
capital_dic={'korea':'seoul','china':'beijing','USA':'wachington DC'}
print(capital_dic['korea']) #seoul
print(capital_dic['china']) #beijing
print(capital_dic['USA'])   #wachington DC
fruits_dic={'apple':5000,'banana':4000 ,'grape':5300,'melon':6500}
print('apple의 가격은',fruits_dic['apple'],'원입니다.')
print('banana의 가격은',fruits_dic['banana'],'원입니다.')
print('grape의 가격은',fruits_dic['grape'],'원입니다.')
print('melon의 가격은',fruits_dic['melon'],'원입니다.')

#6.2 딕셔너리의 삽입과 삭제
#실습 : 딕셔너리의 항목 삽입
person={'이름' : '홍길동', '나이' :26, '몸무게':82}
person['직업']='율도국의 왕'
print(person) #{'이름': '홍길동', '나이': 26, '몸무게': 82, '직업': '율도국의 왕'}
#실습 : 딕셔너리의 항목 수정
person={'이름' : '홍길동', '나이' :26, '몸무게':82}
person['나이']=27
print(person) #{'이름': '홍길동', '나이': 27, '몸무게': 82}
#실습 : 딕셔너리 항목 삭제
person={'이름' : '홍길동', '나이' :26, '몸무게':82}
del person['나이']
print(person) #{'이름': '홍길동', '몸무게': 82}
#딕셔너리 항목 삭제 - keyerror 오류 발생
# person={'이름' : '홍길동', '나이' :26, '몸무게':82}
# del person['출생지']
# print(person) #KeyError: '출생지'
#lab 6-2 : 딕셔너리의 항목 추가와 삭제
#1
person={'이름' : '홍길동', '나이' :26, '몸무게':82}
person['특기']='분신술'
print(person) #{'이름': '홍길동', '나이': 26, '몸무게': 82, '특기': '분신술'}
#2
person['아버지']='홍판서'
print(person) #{'이름': '홍길동', '나이': 26, '몸무게': 82, '특기': '분신술', '아버지': '홍판서'}
#3
del person['나이']
print(person) #{'이름': '홍길동', '몸무게': 82, '특기': '분신술', '아버지': '홍판서'}

#6.3 딕셔너리와 연산자
#실습 : in 연산자를 이용한 딕셔너리 항목의 조회
person={'이름' : '홍길동', '나이' :26, '몸무게':82}
print(len(person)) #3  - 딕셔너리 항목의 개수를 반환
print('이름'in person) #True -키에 있는지 여부 확인
print('아버지' in person) #False
#실습 : in 연산자를 이용한 항목의 존재여부 조회
print('apple' in ['orange','apple','mango']) #True
print('x' in 'aeiou') #False
#실습 : 딕셔너리의 비교 연산
d1={'이름':'홍길동','나이':26}
d2={'나이':26,'이름':'홍길동'}
print(d1==d2) #True
# print(d1>d2) #TypeError: '>' not supported between instances of 'dict' and 'dict' :딕셔너리에서는 비교 연산 지원 안함
#lab 6-3 :딕셔너리와 연산
capital_dic={'korea':'seoul','china':'beijing','USA':'wachington DC'}
print('korea' in capital_dic) #True
print('china' in capital_dic) #True
print('indonesia' in capital_dic) #False
print('bejing' in capital_dic)  #False

#6.4 딕셔너리와 메소드
#실습 : 딕셔너리의 key(),values(),item() 메소드
person=person={'이름' : '홍길동', '나이' :26, '몸무게':82}
print(person.keys()) #dict_keys(['이름', '나이', '몸무게'])
print(person.values()) #dict_values(['홍길동', 26, 82])
print(person.items()) #dict_items([('이름', '홍길동'), ('나이', 26), ('몸무게', 82)])
#실습 : 딕셔너리의 get() 메소드
person={'이름':'홍길동','나이':26,'몸무게':82}
# print(person['취미']) #KeyError: '취미'
print(person.get('취미')) #None -아무런 값도 가지지 않음
print(person.get('이름')) #홍길동
#실습: 딕셔너리의 메소드 살펴보기
person={'이름':'홍길동','나이':26,'몸무게':82}
print(person.popitem()) #('몸무게', 82)
person.pop('나이')
print(person) #{'이름': '홍길동'}
person.clear()
print(person) #{}
#lab 6-4: 딕셔너리의 활용
fruits_dic={'apple':6000,'melon':3000,'banana':5000,'orange':7000}
print(fruits_dic.keys()) #dict_keys(['apple', 'melon', 'banana', 'orange'])
print(fruits_dic.values()) #dict_values([6000, 3000, 5000, 7000])
fruits_dic.pop('apple')
print(fruits_dic) #{'melon': 3000, 'banana': 5000, 'orange': 7000}
fruits_dic.clear()
print(fruits_dic) #{}
#실습 : for문을 이용한 딕셔너리의 순회
person={'이름':'홍길동','나이':26,'몸무게':82}
for key in person:
    print(f'{key} : {person[key]}') #이름 : 홍길동,나이 : 26,몸무게 : 82
