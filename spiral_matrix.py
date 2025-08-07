import numpy as np
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        seen = set()
        l = np.array(matrix).size
        i = 0
        points = []
        
        x = 0
        y = 0
        first_number = matrix[0][0]
        seen.add(first_number)
        points.append(first_number)
        moving_right = True
        movign_down = False
        moving_left = False
        moving_up = False
        
        next_number = matrix[y][x]

        while i < l:
            
            if moving_right:
                x += 1
                try:
                    next_number = matrix[y][x]
                    if next_number in seen:
                        x -= 1
                        next_number = matrix[y][x]
                        moving_right = False
                        movign_down = True
                except IndexError:
                    x -= 1
                    next_number = matrix[y][x]
                    moving_right = False
                    movign_down = True
            if movign_down:
                y += 1
                try:
                    next_number = matrix[y][x]
                    if next_number in seen:
                        y -= 1
                        next_number = matrix[y][x]
                        movign_down = False
                        moving_left = True
                except IndexError:
                    y -= 1
                    next_number = matrix[y][x]
                    movign_down = False
                    moving_left = True
            if moving_left:
                x -= 1 if x != 0 else x 
                try:
                    next_number = matrix[y][x]
                    if next_number in seen:
                        x += 1
                        next_number = matrix[y][x]
                        moving_left = False
                        moving_up = True
                except IndexError:
                    x += 1
                    next_number = matrix[y][x]
                    moving_left = False
                    moving_up = True
            if moving_up:
                y -= 1
                try:
                    next_number = matrix[y][x]
                    if next_number in seen:
                        y += 1
                        next_number = matrix[y][x]
                        moving_up = False
                        moving_right = True
                except IndexError:
                    y += 1
                    next_number = matrix[y][x]
                    moving_up = False
                    moving_right = True
            current_number = next_number
            points.append(current_number)
            seen.add(current_number)
            i += 1
        return points
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]

if __name__ == "__main__":
    solution = Solution()
    result = solution.spiralOrder(matrix)
    print(result)

