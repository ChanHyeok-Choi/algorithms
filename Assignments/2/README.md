# How to run sum_dist.py
There are 6 test cases:
    ex1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ex2 = [2, 8, 7, 1, 3, 5, 6, 4]
    ex3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
    ex4 = [1, 1, 1, 1, 1, 1, 1, 1, 10]
    ex5 = [1, 1, 1, 1, 1, 1, 2, 1, 2, 10]
    ex6 = [10, 10, 10, 10, 10, 9, 2, 1, 2, 1]

You can simply run "python3 sum_dist.py"

# How to run sum_dist.cpp
There are the same test cases in sum_dist.py

You can simply make a runnable file by run "make".
As result, there will be "sum_dist.o" and "sum_dist" made.
After then, you are able to simply run "./sum_dist"

If you see a detail, refer to "Makefile".

# Analysis
There are two main methods: "sum_dist_twoFor" and "sum_dist_median"
* sum_dist_twoFor:
After using sorting algorithm("O(NlogN)"), set maximum distance summation by
adding all integers in an array. Then, iterate all possible positive "k" integer
and make & compare a sum of |Array_i - k| for each i. After two iteration("O(N^2)"), 
we can get minimum distance summation.
* sum_dist_median:
We can estimate that a median distance can optimize a minimum distance summation.
So, after sorting an array("O(NlogN)"), set a median value of the array. Then,
make a sum of |Array_i - k| for each i. After one iteration("O(N)"), we can get minimum
distance summation.