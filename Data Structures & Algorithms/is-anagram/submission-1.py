class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = list()
        tCount = list()

        if(len(s) != len(t)): return False

        for i in range(len(s)):
            try:
                if(sCount[i]):
                    sCount[i][1]+=1
            except:    
                sCount.append((s[i],1))
        
        for j in range(len(t)):
            try:
                if(tCount[j]):
                    tCount[j][1]+=1
            except: 
                tCount.append((t[j],1))

        sCount.sort()
        tCount.sort()

        return sCount == tCount
                


        