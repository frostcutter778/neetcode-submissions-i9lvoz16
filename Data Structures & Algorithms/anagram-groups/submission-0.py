class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #defaultdict(list) is a special type of dictionary from Python’s collections module that automatically creates a default value when a key doesn’t exist
        for s in strs: #iterating through each string present in the list
            count = [0] * 26 #creating a list of 26 numbers and intializing with 0 times each letter appears in the string s 
            for c in s.lower(): #converting edge cases if there are uppercase letters and iterating through each character of the string
                count[ord(c) - ord('a')] += 1 #converting a character into an index from 0 to 25 and incremeting the count of that character
            result[tuple(count)].append(s) #Tuples are immutable and can be used as dictionary keys, so appending those strings to the similar pattern dictionary keys accessible through the tuple
        return list(result.values()) #returning each of the strings which are stored as values to each key from the dictionary in the form of a list as the output format suggests