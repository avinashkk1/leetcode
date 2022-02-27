import functools

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        noOfPositions = len(votes[0])
        
        rankings = {}
        for vote in votes:
            for i, ch in enumerate(vote):
                if ch not in rankings:
                    rankings[ch] = [0] * noOfPositions
                rankings[ch][i] -= 1
        
        #print(rankings)
        
        def sortByRank(team1, team2):
            if rankings[team1] < rankings[team2]:
                return -1
            if rankings[team1] > rankings[team2]:
                return 1
            return -1 if team1 < team2 else 1
            
        return ''.join(sorted(votes[0], key = functools.cmp_to_key(sortByRank)))
                
        