def solution1(priorities, location):
    answer = 0
    li = [0] * len(priorities)
    li[location] = 1
    while 1 in li:
        High = max(priorities)
        pop_p = priorities.pop(0)
        pop_li = li.pop(0)
        if pop_p == High:
            answer += 1
            continue
        priorities.append(pop_p)
        li.append(pop_li)
        
    return answer

def solution2(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

test1 = [[2,1,3,2], 2]
test2 = [[1,1,9,1,1,1], 0]

print(solution1(test1[0], test1[1])) # 1
print(solution1(test2[0], test2[1])) # 5

### what is "any"? ###
# if any element in iterable is True, return true
a = [1,2,0,4,5]
result = any(a)
print(f'any([1,2,3,4,5]) : {result}') # True
b = [0,0,0,0,0]
result = any(b)
print(f'any([1,2,3,4,5]) : {result}') # False