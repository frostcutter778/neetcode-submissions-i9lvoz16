class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # Generating an empty hashmap that takes in val : index

        for i,n in enumerate(nums): # iterating through the given array 
            diff = target - n 
            if diff in prevMap: 
                return [prevMap[diff], i]
            prevMap[n] = i # keeping the current value from the array according to current index in the hashmap 
        return 
           
        