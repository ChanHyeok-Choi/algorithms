def ClassRoomsNeeded(s, f):
    n = len(s)
    A = [[(s[0], f[0])]]
    for i in range(1, n):
        Allocate_Flag = 0
        for j in range(0, len(A)):
            if s[i] < A[j][-1][1]:
                Allocate_Flag += 1
            else:
                A[j].append((s[i], f[i]))
                break
        if Allocate_Flag == len(A):
            A.append([(s[i], f[i])])
    
    # print(A)
    
    return A

startTime1 = [9, 9, 9, 11, 11, 13, 13, 14, 15, 15]
finishTime1 = [10.5, 12.5, 10.5, 12.5, 14, 14.5, 14.5, 16.5, 16.5, 16.5]

print(f"startTime1 length: {len(startTime1)}")
print(f"finishTime1 length: {len(finishTime1)}")

print(f"Minimum number of class rooms: {ClassRoomsNeeded(startTime1, finishTime1)}")