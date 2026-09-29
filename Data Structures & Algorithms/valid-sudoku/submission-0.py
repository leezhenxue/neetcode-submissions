class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        # Check each row for repetition
        for row_index in range(9):
            for column_index in range(9):
                value = board[row_index][column_index]
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
            seen.clear()

        # Check each column for repetition
        for column_index in range(9):
            for row_index in range(9):
                value = board[row_index][column_index]
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
            seen.clear()

        # Check each sub-boxes of the grid for repetition
        for row_index in range(9):
            if row_index % 3 == 0:
                sets = [set(), set(), set()]
            for column_index in range(9):
                value = board[row_index][column_index]
                if value == ".":
                    continue
                if value in sets[column_index//3]:
                    return False
                sets[column_index//3].add(value)

        return True