class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 ={}
        dict2={}
        for x in s1:
            dict1[x] = dict1.get(x,0)+1
        l=0
        for r in range(len(s2)):
            dict2[s2[r]] = dict2.get(s2[r],0)+1
            if r-l+1>len(s1):
                dict2[s2[l]]-=1 
                if  dict2[s2[l]] ==0:
                    del dict2[s2[l]]
                l+=1
            print(dict2)
            if dict1 == dict2:
                return True
        return False

        