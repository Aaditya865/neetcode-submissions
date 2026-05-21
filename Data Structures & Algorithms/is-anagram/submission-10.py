class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl= list(s)
        tl= list(t)
        if len(sl)!=len(tl):
            return False
        sl.sort()
        tl.sort()
        for i in range (len(tl)):
            if sl[i]!=tl[i]:
                return False
        return True
            