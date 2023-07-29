


num_list=[1,5,7,15,16,22,28,29]
"""
def get_odd_num(num_list): 
    odd_list=[] #빈리스트 선언
    for i in num_list: 
        if i%2==1:
            odd_list.append(i)

        else:
            continue 
    return odd_list
"""
def get_odd_num(num_list):
    #TODO
    return [n for n in num_list if n%2 == 1]
print(get_odd_num(num_list))

# a,b=input().split()
# s=a+b
# print(s)

print(3+2*5//2)