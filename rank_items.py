votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]

import statistics as stat
from typing import List

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        letters_rank = {}
        for vote in votes:
            for i, letter in enumerate(vote):
                rank = i + 1
                if letter not in letters_rank:
                    letters_rank[letter] = []

                letters_rank[letter].append(rank)
        letters_rank_average = {}
        for letter in letters_rank: 
            letters_rank_average[letter] = stat.mean(letters_rank[letter])
        ranked = dict(sorted(letters_rank_average.items(), key=lambda item: item[1]))
        result = ''
        for key in ranked:
            result += key
        return result

if __name__ == "__main__":
    solution = Solution()
    result = solution.rankTeams(votes)
    print(result)


