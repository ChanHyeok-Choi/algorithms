def solution1(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) != 0:
        return False

    return True

def solution2(s):
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0

test1 = '(())'
test2 = ')()()'
test3 = '(()(()))'
test4 = '()(()'

print(solution2(test1)) # True
print(solution2(test2)) # False
print(solution2(test3)) # True
print(solution2(test4)) # False