def solution1(s):
    answer = []
    
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            answer.append(s[i - 1])
    answer.append(s[-1])
    
    return answer

def solution2(s):
    answer = []
    
    for i in s:
        # print(answer[-1:])
        if answer[-1:] == [i]: # empty array can be applied with [-1:]
            continue
        answer.append(i)
    
    return answer

test1 = [1,1,3,0,1]
test2 = [4,4,4,3,3]

print(solution1(test1))
print(solution1(test2))

print(solution2(test1))
print(solution2(test2))