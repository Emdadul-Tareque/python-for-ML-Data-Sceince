
nums = [8, 1, 2, 2, 3]
# Count the frequency of each number
count = [0] * 101

for num in nums:
    count[num] += 1
print(count)


# Calculate the cumulative count of smaller numbers
cumulative_count = [0] * 101
for i in range(1, 101):
    cumulative_count[i] = cumulative_count[i - 1] + count[i - 1]

# nums = [8, 1, 2, 2, 3]
# count = [0, 1, 2, 1, 0, 0, 0, 0, 1]
# cumulative_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# cumulative_count = [0, 0, 1, 2, 0, 0, 0, 0, 0, 0] (after loop)
print(cumulative_count)