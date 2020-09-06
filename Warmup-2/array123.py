'''
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
'''

def array123(nums):
    for num in range(len(nums)-2):
        if nums[num] == 1 and nums[num+1] == 2 and nums[num+2] == 3:
            return True
    return False

# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True