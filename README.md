Interview challenge by Paulo Barros

I choose to do this exercise in Python because I have not used the language in
a long time, but I enjoy it. Aside from my limited experience with
Python, I also never had the opportunity to use PyUnit, so I figure
that I could use this exercise to learn something new. The tests are done using
PyUnit.

This solution assumes that one of the bases of the equilateral triangle is
on the bottom.

This problem is an instance of longest path problem, and the graph is a DAG
(directed acyclic graph). Therefore, this can be solved in linear time,
visiting each node (element in the triangle) once.

The solution uses logarithmic space.
If it was specified that changing the original triangle wasn't an issue, then we
wouldn't need extra space at all, but that wasn't the case. Therefore, it is
needed to keep track of 2 "rows" of the triangle, and in the worst case scenario
the size of the row will be the size of the last row, which is equal to the
height of the triangle, therefore the solution uses logarithmic space.

Tested using Python 2.7.

To test it run the helltriangle.py file passing an input. <br />
For example: <br />
$ python helltriangle.py [[6],[3,5],[9,7,1],[4,6,8,4]]

To run all tests run the class AllTests.py: <br />
$ python AllTests.py

