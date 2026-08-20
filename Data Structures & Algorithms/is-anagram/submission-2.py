class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}

        if(len(s) != len(t)): return False

        for i in s:
            try:
                counts[i]+=1
            except:
                counts[i] = 1

        for i in t:
            try:
                counts[i]-=1
                if(counts[i] < 0):
                    return False
            except:
                return False

        return True
        