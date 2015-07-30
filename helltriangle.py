# helltriangle.py

import sys, ast

class HellTriangle():

    """ Returns the maximum total from top to bottom in a triangle.
        This method creates a copy of the triangle and traverses the new
        triangle from top to bottom, updating the value in each position,
        summing to it the maximum value of its two possible upper nearest
        elements, and returns the maximum value in the bottom level.
    """
    @staticmethod
    def calculate_longest_path(triangle):
        # Corner/Exceptional cases
        if (triangle == None or len(triangle) == 0):
            raise ValueError("Invalid triangle passed as input! Empty triangle.")
        if (not isinstance(triangle[0], list)):
            # Input is a single-dimensional array.
            raise ValueError("Invalid triangle passed as input! Must be a multidimensional array.")
        if len(triangle) == 1:
            # Triangle only has one row.
            if (len(triangle[0]) != 1):
                # Triangle only has one row and more or less than one element.
                raise ValueError("Invalid triangle passed as input! Must be equilateral.")
            # Triangle only has one row and one element. Return it.
            return triangle[0][0]

        # Usual case
        prev_row = triangle[0][:]
        prev_row_length = 1
        for i in range(1, len(triangle)):
            cur_row = triangle[i][:]
            cur_row_length = len(cur_row)

            if (cur_row_length - 1 != prev_row_length):
                raise ValueError("Invalid triangle passed as input! Must be equilateral.")

            for j in range(cur_row_length):
                if (j == 0):
                    # Handling first element in a row.
                    cur_row[j] += prev_row[j]
                elif (j == cur_row_length-1):
                    # Handling last element in a row.
                    cur_row[j] += prev_row[j-1]
                else:
                    # Handling in-between elements in a row.
                    cur_row[j] += max(prev_row[j-1], prev_row[j])
            prev_row = cur_row
            prev_row_length += 1
        return max(cur_row)

"""
Receives as input an equilateral triangle, in the format of a multidimensional
array.
For example: [[6],[3,5],[9,7,1],[4,6,8,4]]
"""
if __name__ == "__main__":
    inputList = ast.literal_eval(sys.argv[1])
    print HellTriangle.calculate_longest_path(inputList)
