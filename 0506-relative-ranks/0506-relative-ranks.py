class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        #in a dict store rank and the index of it 
        d = {}
        for i in range(len(score)):
            d[score[i]] = i
            
        #sort the dictionary based on keys
        sorted_d_keys = dict(sorted(d.items()))
        
        #variable to keep eye of the rank
        rank = len(score)
        
        #iterating through the org array to make the changes
        for k,v in sorted_d_keys.items():
            if rank == 3:
                score[v] = "Bronze Medal"
            elif rank == 2:
                score[v] = "Silver Medal"
            elif rank == 1:
                score[v] = "Gold Medal"
            else:
                r = str(rank)
                score[v] = r
            rank -= 1
            
        return score
        