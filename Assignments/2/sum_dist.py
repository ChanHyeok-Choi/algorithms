"""
Writer: 20181257 ChanHyeok Choi
Date: 2023-05-06

6. (2 points) Given an array A consisting of n positive integers, let's assume that we want to find a
positive integer k such that the total sum of the distances between all elements of A and k
becomes minimized, i.e., sum = min ∑ d_i from i=1 to n , where d_i = |A[i] - k| is the distance between A[i] and
k. Write real code (not pseudocode) that returns sum (not k), given an array A of length n. Write
(type) your code with a keyboard and upload it as a separate file.
● Your code should be written either in C or Python. It should be compiled and run (Zero points if
the uploaded code does not run).
● Do not use built-in C or Python libraries that directly solve the problem.
● Upload your code as a separate file
● Only the code uploaded to BlackBoard will be graded (not the code on your computer).
"""

# I will use dynamic programming for optimal minimum sum of distance

def sum_dist_twoFor(A, n):
    sum = 0
    # Your code
    A.sort()
    
    maximum = 0
    for i in range(0, n):
        maximum += A[i]
    
    sum = maximum
    for i in range(1, n+1):
        sum_i = 0
        for j in range(0, n):
            sum_i += abs(A[j] - i)
        sum = min(sum, sum_i)
        
    return sum

def sum_dist_median(A, n):
    sum = 0
    
    # Your code
    A.sort()
    median = A[n//2]
    
    for i in range(n):
        sum += abs(A[i] - median)
    
    return sum

ex1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ex2 = [2, 8, 7, 1, 3, 5, 6, 4]
ex3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
ex4 = [1, 1, 1, 1, 1, 1, 1, 1, 10]
ex5 = [1, 1, 1, 1, 1, 1, 2, 1, 2, 10]
ex6 = [10, 10, 10, 10, 10, 9, 2, 1, 2, 1]
print(sum_dist_twoFor(ex1, len(ex1)) == sum_dist_median(ex1, len(ex1)))
print(sum_dist_twoFor(ex2, len(ex2)) == sum_dist_median(ex2, len(ex2)))
print(sum_dist_twoFor(ex3, len(ex3)) == sum_dist_median(ex3, len(ex3)))
print(sum_dist_twoFor(ex4, len(ex4)) == sum_dist_median(ex4, len(ex4)))
print(sum_dist_twoFor(ex5, len(ex5)) == sum_dist_median(ex5, len(ex5)))
print(sum_dist_twoFor(ex6, len(ex6)) == sum_dist_median(ex6, len(ex6)))