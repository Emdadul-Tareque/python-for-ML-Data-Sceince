"""
input: nums = [8, 1, 2, 2, 3]
output: [4, 0, 1, 1, 3]
"""
#More Efficient 

def smallerNumbersThanCurrent(nums):
    # Count the frequency of each number
    count = [0] * 101
    for num in nums:
        count[num] += 1
    
    # Calculate the cumulative count of smaller numbers
    cumulative_count = [0] * 101
    for i in range(1, 101):
        cumulative_count[i] = cumulative_count[i - 1] + count[i - 1]
    
    # Calculate the result for each element
    result = [cumulative_count[num] for num in nums]
    
    return result

# Test cases
nums1 = [8, 1, 2, 2, 3]
print(smallerNumbersThanCurrent(nums1))  # Output: [4, 0, 1, 1, 3]

nums2 = [6, 5, 4, 8]
print(smallerNumbersThanCurrent(nums2))  # Output: [2, 1, 0, 3]

nums3 = [7, 7, 7, 7]
print(smallerNumbersThanCurrent(nums3))  # Output: [0, 0, 0, 0]

# Efficient approach using hashmap technic
nums = [6,5,4,8]
output = []
sorted_nums = sorted(nums)
dic = {}
nums_length = len(nums)
for i in range(nums_length):
    if sorted_nums[i] not in dic:
        dic[sorted_nums[i]] = i

for num in nums:
    output.append(dic[num])


print(dic)
print(output)





# Brute Forces Technic
nums = [7,7,7,7]
output = []
nums_length = len(nums)
for i in range(nums_length):
    count = 0
    for j in range(nums_length):
        if nums[i] > nums[j]:
            count += 1
    output.append(count)

print(output)




