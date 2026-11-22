class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        b = {}
        c = []
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key not in b:
                b[key] = [strs[i]]
            else:
                b[key] += [strs[i]]
        for i in b:
            c.append(b[i])
            
        return c
        





        
        