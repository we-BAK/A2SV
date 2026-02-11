import string

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        alphabet = string.ascii_lowercase
        morse_map = dict(zip(alphabet, morse_list))
        
        seen_transformations = set()
        
        for word in words:
            current_transformation = ""
            for char in word:
                current_transformation += morse_map[char]
            
            seen_transformations.add(current_transformation)
            
        return len(seen_transformations)