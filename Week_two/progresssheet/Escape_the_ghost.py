class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
      ghost_win=False
      my_pos=[0,0]
      nearest = float('inf')
      for arr in ghosts:
        result=[x - y for x, y in zip(target, arr)]
        result=list(map(abs, result))
        steps=sum(result)
        nearest=min(steps,nearest)
      my_steps=[x - y for x, y in zip(target,my_pos)]
      my_steps=list(map(abs, my_steps))
      my_steps=sum(my_steps)
      if my_steps < nearest:
        return True
      else:
        return False


            
            

        


