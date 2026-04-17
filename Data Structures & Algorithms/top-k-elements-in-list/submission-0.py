class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums: # going through each of the numbers in the list 
            count[num] = 1 + count.get(num, 0) #incrementing the count of the number 
        for num, cnt in count.items(): #So for each number and its count: put number into the bucket corresponding to its frequency
            freq[cnt].append(num) #freq[cnt] stores all numbers that appear exactly cnt times

        res = []
        for i in range(len(freq) - 1, 0, -1): 
            for num in freq[i]: #For each bucket freq[i], adding all numbers in that bucket to res
                res.append(num)
                if len(res) == k: #Once the length matches the k-most frequent numbers, then returning res
                    return res