# Find Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Example 1:
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
# Input: nums = [4,1,2,1,2]					
# Output: 4
# Example 3:
# Input: nums = [1]
# Output: 1
num = [2,2,1]
num1 = [1,1,1,1,13,3]
# def findSingleNumber(nums):
#     num_count = {}
#     for num in nums:
#         if num in num_count:
#             num_count[num] += 1
#         else:
#             num_count[num] = 1
#     for num, count in num_count.items():
#         if count == 1:
#             print(num)
#             return num
# findSingleNumber(num1)
# findSingleNumber(num)

# def findSingleNumber(num):
#     num.sort()
#     for i in range(0, len(num), 2):
#         if i == len(num) - 1 or num[i] != num[i+1]:
#             print(num)
#             return num[i]
  
#     findSingleNumber(num)

nums1 = [2,2,1]
nums2 = [4,1,2,1,2]  
nums3 = [1]

def findSingle(li):
    for num in li:
        if li.count(num) == 1:
            print(num)
            return num

findSingle(nums1)
findSingle(nums2)
findSingle(nums3)

def findSingle2(li):
    empty = {}

    for num in li:
        if num in empty:
            empty[num] += 1
        else:
            empty[num] = 1
            
    for k, v in empty.items():
        if v == 1:
            print(k)
            return k
    # print(empty)
    #       


findSingle2(nums1)
findSingle2(nums2)
findSingle2(nums3)




















