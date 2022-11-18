def solution1(progresses, speeds):
    answer = []
    while len(progresses) != 0:
        if progresses[0] >= 100:
            cnt = 0
            for i in range(len(progresses)):
                if progresses[0] >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    cnt += 1
                else:
                    break
            if cnt != 0:
                answer.append(cnt)
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
    return answer

def solution2(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<((100-p)//s):
            Q.append([((100-p)//s),1])
        else:
            Q[-1][1]+=1
        print(Q)
    return [q[1] for q in Q]

test1 = [[93, 30, 55], [1, 30, 5]]
test2 = [[95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]]

print(solution2(test1[0], test1[1]))
print(solution2(test2[0], test2[1]))