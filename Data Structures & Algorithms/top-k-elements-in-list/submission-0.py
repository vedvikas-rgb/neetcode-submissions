from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count=Counter(nums)
        ordered_num_count=num_count.most_common(k)
        k_output=[]
        for item in ordered_num_count:
            number=item[0]
            k_output.append(number)

        return(k_output)
            

        
        
        
