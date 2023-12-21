import copy
a_list = [[1,2],[3]]
b_list= copy.deepcopy(a_list)
b_list[1].append(4)
print(a_list, b_list)