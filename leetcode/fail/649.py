class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        current_round = list(senate)
        
        r_ban_credit = 0
        d_ban_credit = 0
        
        while True:
            next_round = [] 
            
            for member in current_round:
                if member == 'R':
                    if d_ban_credit > 0:
                        d_ban_credit -= 1
                    else:
                        r_ban_credit += 1
                        next_round.append('R')
                        
                elif member == 'D':
                    if r_ban_credit > 0:
                        r_ban_credit -= 1
                    else:
                        d_ban_credit += 1
                        next_round.append('D')
            
            if 'R' not in next_round:
                return "Dire"
            if 'D' not in next_round:
                return "Radiant"
                
            current_round = next_round