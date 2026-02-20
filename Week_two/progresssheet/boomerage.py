class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total_boomerangs = 0
        
        for p1 in points:
            distance_map = {}
            
            for p2 in points:
                dist_sq = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
                
                distance_map[dist_sq] = distance_map.get(dist_sq, 0) + 1
            
            for count in distance_map.values():
                total_boomerangs += count * (count - 1)
                
        return total_boomerangs