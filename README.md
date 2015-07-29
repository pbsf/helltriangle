SkyHub interview challenge By Paulo Barros

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
the bottom of the triangle times two, which is still linear, but with a smaller
coefficient. I may improve that in the future if I have time to.

This project is a solution in python to the HellTriangle problem.
Tested on Python 2.7.

To test it run the helltriangle.py file passing an input.
For example:
$ python helltriangle.py [[6],[3,5],[9,7,1],[4,6,8,4]]

To run all tests run the class tests.py:
$ python AllTests.py

