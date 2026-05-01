class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        for n in s:
            if n not in d:
                d[n]=1
            else:
                d[n]=d.get(n)+1
        for n in t:
            if n not in d or d[n] == 0:
                    return False
            d[n]-=1
        return True