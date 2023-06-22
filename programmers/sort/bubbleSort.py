def bubbleSort(A, n):
    '''
    Bubble Sort: Compare two adjacent elements, then move a larger element on right-side.
    Input:
        A: An array to sort
        n: A number of the array
    Output:
        Sorted Array 'A'
    Time complexity:
        O(N^2)
    '''
    
    for i in range(n):
        pivot_idx = 0
        for j in range(0, n):
            if A[j] < A[pivot_idx]:
                # Swap
                temp = A[j]
                A[j] = A[pivot_idx]
                A[pivot_idx] = temp
            pivot_idx = j
    
    return A
        

def test():
    sample1 = [5,4,2,7,8,1,3,6]
    result1 = bubbleSort(sample1, len(sample1))
    print(result1)

if __name__ == '__main__':
    test()