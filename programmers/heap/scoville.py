def blending(scoville, K):
    if len(scoville) == 0:
        return []
    elif len(scoville) == 1:
        return scoville
    elif len(scoville) == 2 and (scoville[0] < K or scoville[1] < K):
        new_value = scoville[0] + scoville[1] * 2
        return [new_value]
    else:
        mid = round(len(scoville) / 2)
        left = blending(scoville[:mid], K)
        right = blending(scoville[mid:], K)
        return sorted(left + right)


def solution1(scoville, K):
    answer = scoville
    cnt = 0
    while any(i < K for i in answer):
        answer = blending(answer, K)
        cnt += 1
    return cnt

def solution2(scoville, K):
    import heapq

    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    cnt = 0
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
            cnt += 1
        except IndexError:
            return -1
    return cnt


test1 = [[1, 2, 3, 9, 10, 12], 7]

print(solution1(test1[0], test1[1])) # wrong solution
print(solution2(test1[0], test1[1]))