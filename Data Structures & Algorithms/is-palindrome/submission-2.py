class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = "".join(c for c in s.lower().replace(" ", "").strip() if c.isalnum())
        i,j = 0, len(st)-1
        while i <= j:
            print("i:",i," j:",j)
            print("s[i]: ",st[i], " s[j]: ", st[j])

            if(st[i] != st[j]):
                return False
            i+=1
            j-=1

        return True