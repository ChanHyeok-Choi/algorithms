'''
Date: 2023-05-26, Writer: 20181257 Chanhyeok Choi

(2 points) Let's assume that there is a two-dimensional plane with n number of points represented
as (x_n, y_n). We want to connect all the points on the plane in such a way that the total distance of
connections (i.e., the summation of distances between all the connected points) is minimized. Write
a real code that returns the minimum total distance of all the connected points. 
* The distance between two points (x_i, y_i) and (x_j, y_j) is calculated by sqrt((x_i - x_j)^2 + (y_i - y_j)^2).
* A point (x_n, y_n) and the distance between two points are real numbers, not integers.
* Your code should be written either in C or Python. Your code should be compiled and run. It is
all your responsibility to make sure that your code is error-free and has no typos.
* Do not use built-in libraries provided by C and Python, which can directly solve the problem.
* Upload your code as a separate file in the same way we did with assignment 2.
* Only the code submitted will be graded (not the code on your computer).
* The function prototype you need to write is given below (C and Python). Your function prototype
should be exactly the same as the following. Otherwise, 0 points
'''

def calculate_distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(1/2)

def calculate_total_distance(points):
    total_distance = 0.0
    n = len(points)
    for i in range(n - 1):
        total_distance += calculate_distance(points[i], points[i+1])
    return total_distance

def permute(points):
    result = [points[:]]
    column = [0] * len(points)
    i = 0
    while i < len(points):
        if column[i] < i:
            if i % 2 == 0:
                points[0], points[i] = points[i], points[0]
            else:
                points[column[i]], points[i] = points[i], points[column[i]]
            result.append(points[:])
            column[i] += 1
            i = 0
        else:
            column[i] = 0
            i += 1
    return result

def min_distance(points, n):
    distance = 0.0
    
    distance = float('inf')
    points_permutation = permute(points)
    for pp in points_permutation:
        distance = min(distance, calculate_total_distance(pp))
        
    return distance

points1 = [[0.0, 0.0], [3.0, 4.0], [4.0, 3.0]]
points2 = [[0.0, 0.0], [1.0, 1.0], [2.0, 3.0], [4.0, 5.0]]
points3 = [[3.0, 4.0], [4.0, 3.0], [0.0, 0.0]]
answers = [6.414, 6.478, 6.414]

print(f"expected min_distnace: {min_distance(points1, len(points1))}, actual min_distance: {answers[0]}")
print(f"expected min_distnace: {min_distance(points2, len(points2))}, actual min_distance: {answers[1]}")
print(f"expected min_distnace: {min_distance(points3, len(points3))}, actual min_distance: {answers[2]}")