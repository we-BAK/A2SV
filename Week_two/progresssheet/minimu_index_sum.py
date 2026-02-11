class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        map1 = {}
        for i in range(len(list1)):
            restaurant = list1[i]
            map1[restaurant] = i        
        min_sum = float('inf')
        result = []
        for j, restaurant in enumerate(list2):
            if restaurant in map1:
                i = map1[restaurant]
                current_sum = i + j
                
                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [restaurant] 
                elif current_sum == min_sum:
                    result.append(restaurant) 
                    
        return result