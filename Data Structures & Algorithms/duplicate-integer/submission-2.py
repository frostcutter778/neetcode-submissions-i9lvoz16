#Time complexity: O(n)
#Space complexity: O(n)

#n is the number of elements in the input list nums.

class Solution:
    def hasDuplicate(self, nums):
        nums_set = set(nums) #set only stores unique values, so the new set will differ in length from the original array because it will not store duplicates
        if len(nums_set) == len(nums): #check the length to see if equal, then no duplicate, else duplicate found and return true
            return False
        else:
            return True