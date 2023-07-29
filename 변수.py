#def test(t):
    #t=20
    #print("in funtion:",t)

#x=10
#test(x)
#print(x)

""" from functools import wraps
def test(funtion):
    @wraps(function)
def wrapper(*arg,**kwargs):
    print("인사가 시작되었습니다")
    function(*arg,**kwargs)
    print("인사가 종료되었습니다")
    return wrapper """

a=2
r=[]
for i in range(0,10):
    r+=2<<i
    print(str(r).replace(',',''))