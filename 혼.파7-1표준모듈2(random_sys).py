#random 모듈 : import random (from 구문 혹은 as 구문과도 조합해서 사용 가능)
import random
print("#random 모듈")
#random(): 0.0 <= 1.0 사이의 float를 리턴
print("-random():",random.random())
#uniform(min,max):지정한 범위 사이의 float를 리턴
print("-uniform(10,20):",random.uniform(10,20))
#randrange():지정한 범위 사이의 float을 리턴
#-randrange(max):0부터 max 사이의 값을 리턴
#-rnadrange(min,max): min부터 max사이의 값을 리턴
print("-randrange(10):",random.randrange(10))
#choice(list):리스트 내부에 있는 요소를 랜덤하게 선택
print("-choice([1,2,3,4,5]):", random.choice([1,2,3,4,5]))
#shuffle(list):리스트의 요소들을 랜덤하게 섞습니다
print("-shuffle([1,2,3,4,5])",random.shuffle([1,2,3,4,5])) #None
#sample(list, k=<숫자>):리스트의 요소 중에 k개를 뽑습니다
print("-sample([1,2,3,4,5]):",random.sample([1,2,3,4,5], k=2))
#파일 저장시 모듈과 같은 이름으로 저장 불가능 [TypeError: 'module' object is not callable]
#random 모듈을 from 구문을 활용해서 임포트
from random import random,randrange,choice

#sys모듈(시스템과 관련된 정보를 가지고 있음.명령 매개변수를 받을 때 많이 사용)
import sys
print(sys.argv)
print("---")
print("getwindowsversion:()",sys.getwindowsversion())
print("---")
print("copyright:",sys.copyright)
print("---")
print("version:",sys.version)

sys.exit()
