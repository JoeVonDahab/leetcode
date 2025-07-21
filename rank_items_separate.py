votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
from collections import Counter
import statistics as stat
from typing import List

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        rank_letter  = {}
        len_vote = len(votes[0])
        for i in range(len_vote):
            for vote in votes:
                rank = i + 1
                if rank not in rank_letter:
                    rank_letter[rank] = []
                letter = vote[i]
                rank_letter[rank].append(letter)
        result = ""
        added = set()
        for _, val in rank_letter.items():
            counter = Counter(val)
            sorted_rank = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
            for letter, count in sorted_rank:
                if letter not in added:
                    result += letter
                    added.add(letter)
                    break  # Add only one letter per position
        return result
                
                

if __name__ == "__main__":
    solution = Solution()
    result = solution.rankTeams(votes)
    print(result)



