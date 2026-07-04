class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        0(n^2)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False     
        """


        arr_len=len(nums)
        solset=set(nums)
        len_set=len(solset)

        if arr_len==len_set:
            return False
        else:
            return True        
            
    




            
                 

           
        