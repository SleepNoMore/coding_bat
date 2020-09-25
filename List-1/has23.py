'''
Given an int array length 2, return True if it contains a 2 or a 3.
'''


def has23(nums):
    return 2 in nums or 3 in nums

# has23([2, 5]) → True
# has23([4, 3]) → True
# has23([4, 5]) → False
