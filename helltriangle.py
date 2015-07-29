# helltriangle.py
"""
 By Paulo Barros

 I choose to do this exercise in Python because I have not used the language in
 a long time, but I enjoy it. Aside from a limited experience with
 Python, I also never had the opportunity to use PyUnit either, so I figure
 that I could use this exercise to learn something new.

 This solution assumes that one of the bases of the equilateral triangle is
 on the bottom.

 This problem is an instance of longest path problem, and the graph is a DAG
 (directed acyclic graph). Therefore, this can be solved in linear time,
 visiting each node (element in the triangle) once.

 The solution is done in linear time, and it uses linear space (2n).
 If it was specified that changing the original triangle wasn't an issue, then I
 wouldn't need extra space at all, but that wasn't the case.
 The solution could be improved to use less space - the amount of elements in
 the bottom of the triangle*2, which is still linear, but with a smaller
 coefficient. I may improve that in the future if I have time to.

"""

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

        # Usual cases
        new_triangle = triangle[:]
        previous_length = 1
        for i in range(1, len(new_triangle)):
            row_length = len(new_triangle[i])

            if (row_length - 1 != previous_length):
                raise ValueError("Invalid triangle passed as input! Must be equilateral.")

            previous_length = row_length
            for j in range(row_length):
                if (j == 0):
                    # Handling first element in a row.
                    new_triangle[i][j] += new_triangle[i-1][j]
                elif (j == len(new_triangle[i])-1):
                    # Handling last element in a row.
                    new_triangle[i][j] += new_triangle[i-1][j-1]
                else:
                    # Handling in-between elements in a row.
                    new_triangle[i][j] += max(new_triangle[i-1][j-1], new_triangle[i-1][j])

        return max(new_triangle[len(new_triangle)-1])

"""
Receives as input an equilateral triangle, in the format of a multidimensional
array.
For example: [[6],[3,5],[9,7,1],[4,6,8,4]]
"""
if __name__ == "__main__":
    inputList = ast.literal_eval(sys.argv[1])
    print HellTriangle.calculate_longest_path(inputList)
