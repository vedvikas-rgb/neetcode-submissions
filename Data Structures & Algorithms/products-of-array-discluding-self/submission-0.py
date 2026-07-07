import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_list=[]
        for i in range(len(nums)):
            extracted_val=nums.pop(i)
            result=math.prod(nums)
            output_list.append(result)
            nums.insert(i,extracted_val)

        return output_list


