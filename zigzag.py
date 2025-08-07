class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = []
        row = []
        rows = numRows 
        up_down = True
        down_up = False
        if numRows == 1:
            return s

        for _ in range(numRows):
            matrix.append([])

        i = 1
        letters_n = len(s)
        matrix[0].append(s[0])

        while i < letters_n:
            if up_down:
                j = 0 
                for j in range(j + 1, numRows):
                    if i < letters_n:
                        matrix[j].append(s[i])
                        i += 1
                up_down = False
                down_up = True
                continue  

            if down_up:
                j = numRows - 2
                for j in range(j, -1, -1):
                    if i < letters_n:
                        matrix[j].append(s[i])
                        i += 1
                down_up = False
                up_down = True
                continue
        final_string_list = []
        for row in matrix:
            for letter in row:
                final_string_list.append(letter)

        final_string = "".join(final_string_list)
        return final_string


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    solution = Solution()
    result = solution.convert(s, numRows)
    print(result)