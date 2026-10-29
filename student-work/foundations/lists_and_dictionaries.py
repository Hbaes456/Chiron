# Lists and dictionaries
# Store `[0.2, 0.8, 0.4, 0.9]` in a list. Build a new list containing only requests above 0.5. Print both lists and their lengths. Then put the limit and the filtered list in a dictionary with descriptive keys.
# Write your attempt below. See the course page for expected results.
nums = [0.2, 0.8, 0.4, 0.9]
filtered_nums = []
for value in nums:
    if value > 0.5:
        filtered_nums.append(value)
print("Original list:", nums)
print("Filtered list:", filtered_nums)
print("Length of original list:", len(nums))
print("Length of filtered list:", len(filtered_nums))
limit_dict = {"limit": 0.5, "filtered_list": filtered_nums}