class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        s_arr=list(s)
        t_arr=list(t)
        s_counts=Counter(s_arr)
        t_counts=Counter(t_arr)


        print(s_counts)
        print("---")
        print(t_counts)
        
        if s_counts==t_counts:
            return True
        else:
            return False

        
