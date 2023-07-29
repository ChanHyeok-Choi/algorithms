def selectionSort(A, n):
    '''
    Selection Sort: Search a minimum element, then location it at the head.
    Input:
        A: An array to sort
        n: A number of the array
    Output:
        Sorted Array 'A'
    Time complexity:
        O(N^2)
    '''
    
    for i in range(n):
        minimum = A[i]
        minimum_idx = i
        for j in range(i, n):
            if A[j] < minimum:
                minimum = A[j]
                minimum_idx = j
        # Swap
        temp = A[i]
        A[i] = minimum
        A[minimum_idx] = temp
    
    return A
        

def test():
    sample1 = [5,4,2,7,8,1,3,6]
    result1 = selectionSort(sample1, len(sample1))
    print(result1)

if __name__ == '__main__':
    test()