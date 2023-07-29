def mergeSort(A):
    '''
    Merge Sort: Use divide-and-conquer, and merge.
    Input:
        A: An array to sort
    Output:
        Sorted Array 'A'
    Time complexity:
        O(NlogN)
    '''
    
    if len(A) <= 1:
        return A
    
    L, R = partition(A)
    L = mergeSort(L)
    R = mergeSort(R)
    
    return merge(L, R)

def partition(A):
    '''
    Partition: divide an array into two array (half of the array).
    Input: 
        An array 'A'
    Output:
        two divided arrays
    '''
    n = len(A)
    L, R = [], []

    for i in range(0, n):
        if i < n // 2:
            L.append(A[i])
        else:
            R.append(A[i])
    
    return L, R
    
def merge(L, R):
    '''
    Partition: merge two arrays into a sorted array.
    Input: 
        An array 'L' and 'R'
    Output:
        Merged array
    '''
    result = []
    
    while len(L) != 0 and len(R) != 0:
        l = L.pop(0)
        r = R.pop(0)
        if l < r:
            result.append(l)
            R.insert(0, r)
        else:
            result.append(r)
            L.insert(0, l)
    
    if len(L) != 0:
        result.append(L.pop(0))
    if len(R) != 0:
        result.append(R.pop(0))
    
    return result
    

def test():
    sample1 = [5,4,2,7,8,1,3,6]
    result1 = mergeSort(sample1)
    print(result1)

if __name__ == '__main__':
    test()