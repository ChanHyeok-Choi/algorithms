padding = 0

def heapSort(A):
    '''
    Heap Sort: Build heap, then repeat to move largest one into last position and retain maxHeap-property.
    Input:
        A: An array to sort
    Output:
        Sorted Array 'A'
    Time complexity:
        O(NlogN)
    '''
    result = []
    buildHeap(A)
    n = len(A)
    for i in range(n-1, 0, -1):
        # Exchange A[1] with A[i]
        temp = A[1]
        A[1] = A[i]
        A[i] = temp
        
        largest = A.pop(-1)
        result.insert(0, largest)
        maxHeapify(A, 1)

    return result

def maxHeapify(A, i):
    l = left(i)
    r = right(i)
    if l < len(A) and A[i] < A[l]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[largest] < A[r]:
        largest = r
    if largest != i:
        # Exchange A[largest] with A[i]
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        maxHeapify(A, largest)

def buildHeap(A):
    n = len(A)
    for i in range(n//2, 0, -1):
        maxHeapify(A, i)
    return A

def left(i):
    return i * 2

def right(i):
    return i * 2 + 1

def parent(i):
    return i // 2

def test():
    sample1 = [padding, 5,4,2,7,8,1,3,6]
    sample2 = [padding, 4,1,3,2,16,9,10,14,8,7]
    heap1 = buildHeap(sample1)
    print(heap1)
    heap2 = buildHeap(sample2)
    print(heap2)
    result1 = heapSort(sample1)
    print(result1)
    result2 = heapSort(heap2)
    print(result2)

if __name__ == '__main__':
    test()