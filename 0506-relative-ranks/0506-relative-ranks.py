class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = {}
        for i in range(len(score)):
            d[score[i]] = i
        sorted_d_keys = dict(sorted(d.items()))
        rank = len(score)
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
        