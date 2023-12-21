another_list = ["a","b"]
a_list=[1,2,another_list]
b_list =[]
for e in a_list:
  b_list.append(e)
b_list.append(5)
b_list[2].append(4)
print(a_list) 
print(b_list)

another_list = ["a","b"]
a_list=[1,2,another_list]
b_list = list(a_list)
b_list[2].append(4)
print(a_list)


a_list = [[1,2],[3]]
b_list= a_list
b_list[1].append(4)
print('a list: ',  a_list)
print('b_list: ',  b_list)
    



import copy
a_list = [[1,2],[3]]
b_list= copy.deepcopy(a_list)
b_list[1].append(4)
print(a_list, b_list)