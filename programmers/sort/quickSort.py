def quickSort(A, p, r):
    '''
    Quick Sort: Use pivot and divide two parts (less than or equal to pivot, larger than pivot).
    Input:
        A: An array to sort
    Output:
        Sorted Array 'A'
    Time complexity:
        best: O(NlogN)
        average: O(NlogN)
        worst: O(N^2) --> But, we can expect quickSort to generally do sort in O(NlogN)
    '''
    if p < r:
        A, q = partition(A, p, r)
        A = quickSort(A, p, q)
        A = quickSort(A, q+1, r)
        
    return A

def partition(A, p, r):
    pivot = A[r]
    i = p-1
    
    for j in range(r):
        if pivot > A[j]:
            # Exchange A[j] with A[i+1]
            temp = A[j]
            A[j] = A[i+1]
            A[i+1] = temp
            i += 1
    # Exchange A[r] with A[i+1]
    temp = A[r]
    A[r] = A[i+1]
    A[i+1] = temp
    
    return A, i+1

def test():
    sample1 = [5,4,2,7,8,1,3,6]
    result1 = quickSort(sample1, 0, len(sample1)-1)
    print(result1)

if __name__ == '__main__':
    test()