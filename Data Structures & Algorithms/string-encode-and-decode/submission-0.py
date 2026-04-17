class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: #appending the strings together 
            res += str(len(s)) + "#" + s #appending the length of the string followed by the special character and then followed by the string and keeping this pattern for easier identification
        #print(res)
        return res 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            #print("i", i)
            #print("j", j)
            length = int(s[i:j]) #getting the length from the encoded string 
            #print(length)
            i = j + 1 #incrementing the ith value to start from the first letter of the string because j is currently at # and after that the string starts
            j = i + length #incrementing the jth value to be the endpoint of the string, and that would be from the starting of the string + the length of the actual string
            res.append(s[i:j]) #getting the actual string from the new i and j 
            i = j #resetting i to be the same as j, for getting the next string

        return res