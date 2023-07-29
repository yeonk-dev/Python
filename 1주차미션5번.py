1.
inputs = "cat32dog16cow5"

def find_string(inputs):
    temp = ""
    res = list()

    for v in inputs:
        if v.isdigit():
            if temp != "":
                res.append(temp)
            temp = ""
        else:
            temp += v
    return res

string_list = find_string(inputs)
print(string_list)

2.
inputs = "cat32dog16cow5"
def find_string(inputs):
    res = ""
    for letter in inputs:
        if letter.isnumeric():
            res += ' '
        else:
            res += letter
    res = res.split()
    return res
string_list = find_string(inputs)
print(string_list)
3.
import re
inputs = "cat32dog16cow5"
def find_string(inputs):
	res = ""
	res = re.sub('\d', ' ', inputs).split()
	return res
	
string_list = find_string(inputs)
print(string_list)


