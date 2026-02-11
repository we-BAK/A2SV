class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        result = []
        for word in words:
            lower_word = word.lower()
            first_char = lower_word[0]
            
            if first_char in row1:
                target_row = row1
            elif first_char in row2:
                target_row = row2
            else:
                target_row = row3
            
            is_valid = True
            for char in lower_word:
                if char not in target_row:
                    is_valid = False
                    break 
            
            if is_valid:
                result.append(word)
                
        return result