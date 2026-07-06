from collections import Counter
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map={}

     
        for s in strs:
            #counting characters
            char_count=Counter(s)
            #creating a hashable key by sorting items and turnign them into a tuple and the tuple becomes your key,char_count.items() returns a list of (character, count) pairs.
            """
            sorted() to sort these (character, count) pairs alphabetically by character.This ensures that two different strings that are anagrams will have the same sorted sequence—just like a "signature."
            Finally, we turn that sorted list of pairs into a tuple. Tuples are hashable, which means we can use them as keys in a dictionary
            """
            key=tuple(sorted(char_count.items()))

            if key not in anagram_map:
                anagram_map[key]=[]
            anagram_map[key].append(s) #appending to list stored inside dict not the dict itself

        return list(anagram_map.values())
