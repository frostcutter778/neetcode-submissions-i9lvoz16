class Solution:
        def isAnagram(self, s: str, t: str):
              d1 = {}
              d2 = {}
              for chs in s:
                d1[chs] = d1.get(chs, 0) + 1
              for cht in t:
                d2[cht] = d2.get(cht, 0) + 1
              if d1 == d2:                       
                return True
              return False
        