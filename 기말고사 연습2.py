# def cel2fah(cel):
#     for cel in range(10,51,10):
#         print(f'섭씨 {cel}도 = 화씨 {(9/5)*cel+32}')
# cel2fah(10)

# a,b,c=map(int,input('세 수를 입력하시오 : ').split())
# def mean3(a,b,c):
#     return (a+b+c)/3
# def max3(a,b,c):
#     return max(a,b,c)
# def min3(a,b,c):
#     return min(a,b,c)
# print(f'{a}, {b}, {c}의 평균값은 {mean3(a,b,c)}')
# print(f'{a}, {b}, {c}의 최대값은 {max3(a,b,c)}')
# print(f'{a}, {b}, {c}의 최소값은 {min3(a,b,c)}')

# a,b,c,d,e,f=map(int,input('여섯 개의 수를 입력하시오 :').split())
# def mean3(a,b,c,d,e,f):
#     return (a+b+c+d+e+f)/6
# def max3(a,b,c,d,e,f):
#     return max(a,b,c,d,e,f)
# def min3(a,b,c,d,e,f):
#     return min(a,b,c,d,e,f,)
# print(f'평균값은 {mean3(a,b,c,d,e,f)}')
# print(f'최대값은 {max3(a,b,c,d,e,f)}')
# print(f'최소값은 {min3(a,b,c,d,e,f)}')


def mean_of_n(nums):
    result=0
    for num in nums:
        result+=num
    r1=result/len(nums)
    return r1
def max3(nums):
    max_val=int(nums[0])
    for num in nums:
        if max_val<int(num):
            max_val=int(num)
    return max_val
def min3(nums):
    min_val=int(nums[0])
    for num in nums:
        if min_val>int(num):
            min_val=int(num)
    return min_val
nums=list(map(int,input('정수를 여러 개 입력하시오:').split(' ')))
print('평균값은:','{:.1f}'.format(mean_of_n(nums)))
print('최댓값은:',max3(nums))
print('최소값은:',min3(nums))