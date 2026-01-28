class Solution:
    def findWinners(self, matches):
        loss_count = {}      
        all_players = set()  
        
        for winner, loser in matches:
            
            all_players.add(winner)
            all_players.add(loser)
        
            loss_count[loser] = loss_count.get(loser, 0) + 1
            
        zero_loss = []
        one_loss = []
        
        for player in all_players:
            if player not in loss_count:
                zero_loss.append(player)
            elif loss_count[player] == 1:
                one_loss.append(player)
        
    
        return [sorted(zero_loss), sorted(one_loss)]