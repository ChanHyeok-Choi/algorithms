def solution1(array, commands):
    answer = []
    for li in commands:
        start = li[0] - 1
        end = li[1]
        position = li[2] - 1
        sliced_array = sorted(array[start:end])
        answer.append(sliced_array[position])
    return answer

def solution2(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

test1 = [[1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]] 

print(solution2(test1[0], test1[1])) # [5, 6, 3]