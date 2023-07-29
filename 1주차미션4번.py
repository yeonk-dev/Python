dict_first = {'사과': 30, '배': 15, '감': 10, '포도': 10}
dict_second = {'사과': 5, '감': 25, '배': 15, '귤': 25}

from collections import defaultdict

def merge_dict(dict_first, dict_second):
  d = defaultdict(lambda: 0)

  for v in dict_first:
    d[v] += dict_first[v]
  for v in dict_second:
    d[v] += dict_second[v]

  print(dict(d))

merge_dict(dict_first, dict_second)

def merge_dict(dict_first, dict_second):
    dict_merge = dict_first
    for key in list(dict_second):
        if key in dict_merge:
            dict_merge[key] += dict_second[key]
        else:
            dict_merge[key] = dict_second[key]
    return dict_merge

dict_merge = sorted(dict_merge.items())

dict_first = {"사과": 30, "배": 15, "감": 10, "포도": 10}
dict_second = {"사과": 5, "감": 25, "배": 15, "귤": 25}

def merge_dict(dict_first, dict_second):
    dict_merge = dict_first
    for key in list(dict_second):
        if key in dict_merge:
            dict_merge[key] += dict_second[key]
        else:
            dict_merge[key] = dict_second[key]
    dict_merge = dict(sorted(dict_merge.items(), key=lambda x: x[0]))
    
    return dict_merge

print(merge_dict(dict_first, dict_second))