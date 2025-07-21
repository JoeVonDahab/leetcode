points = [[1,1],[3,4],[-1,0]]
from collections import Counter
import statistics as stat
from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        current_point = points[0]
        time = 0
        i = 1
        while i < len(points):
            next_point = points[i]
            if next_point[0] - current_point[0] != 0 and next_point[1] - current_point[1] != 0:
                current_point[0] += 1 if next_point[0] > current_point[0] else -1
                current_point[1] += 1 if next_point[1] > current_point[1] else -1
                time += 1
            elif next_point[0] - current_point[0] != 0:
                current_point[0] += 1 if next_point[0] > current_point[0] else -1
                time += 1
            elif next_point[1] - current_point[1] != 0:
                current_point[1] += 1 if next_point[1] > current_point[1] else -1
                time += 1
            else:
                i += 1
        return time

                
                

if __name__ == "__main__":
    solution = Solution()
    result = solution.minTimeToVisitAllPoints(points)
    print(result)



