"""
Problem: Consider a list as list1 consisting of some integer elements. First, 
delete an element from the K-th position of the list, 
and then print the list excluding the first and last elements.

Example 1:

Input:

list1 = [1,2,3,4,5]
K = 2
Output: [2, 4]


Example 2:

Input:

list1 = [1,2,3,4,5,6,7,8]
K = 4
Output:

[2, 3, 4, 6, 7]
"""

def delete_access(list, kth):
    list.pop(kth)
    
    return list[1:-1]


#test_case 01
list1 = [1,2,3,4,5]
kth = 2
print(delete_access(list1, kth))

#test_case 02
list2 = [1,2,3,4,5,6,7,8]
kth = 4
print(delete_access(list2, kth))