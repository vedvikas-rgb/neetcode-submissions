class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer=""
        for j in range(len(strs[0])):
            for i in range(len(strs)):
            
                
                        if j>= len(strs[i]) or strs[i][j]!=strs[0][j]:
                            return answer
            answer += strs[0][j]


        return answer
                        
                       
                          

               

