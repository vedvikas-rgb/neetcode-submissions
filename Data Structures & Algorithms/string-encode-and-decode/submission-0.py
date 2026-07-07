class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded



    def decode(self, s: str) -> List[str]:
        decoded=[]
        i=0

        while i<len(s):
            #find the separator
            j=i
            while s[j]!="#":
                j+=1

            #get the len
            length= int(s[i:j])

            #moving past #
            j+=1

            #grabbing the string( from start(j) to start+len)
            decoded.append(s[j:j+length])

            i=j+length

        return decoded
