#실전코딩1 p.243
def flatten(data):
    output=[]
    for item in data:
        if type(item)==list:
            output+=flatten(item)
        else:
            output.append(item)
    return output
example=[[1,2,3],[4,[5,6]],7,[8,9]]
print("원본:",example) #원본: [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("변환:",flatten(example)) #변환: [1, 2, 3, 4, 5, 6, 7, 8, 9]

#실전코딩2 p.244-245
앉힐수있는최소사람수=2
앉힐수있는최대사람수=10
전체사람의수=100
memo={}
def 문제(남은사람수,앉힌사람수):
    key=str([남은사람수,앉힌사람수])
    #종료 조건
    if key in memo:
        return memo[key]
    if 남은사람수<0:
        return 0
    if 남은사람수==0:
        return 1
    #재귀처리
    count=0
    for i in range(앉힌사람수,앉힐수있는최대사람수+1):
        count+=문제(남은사람수-i,i)
    #메모화처리
    memo[key]=count
    #종료
    return count
print(문제(전체사람의수,앉힐수있는최소사람수)) #437420

