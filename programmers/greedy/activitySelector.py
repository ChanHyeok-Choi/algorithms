def recursive_activity_selector(s, f, k, n):
    m = k + 1
    while m < n and s[m] < f[k]:
        m += 1
    if m < n:
        return [m] + recursive_activity_selector(s, f, m, n)
    else:
        return []

def sort_by_finish(s, f):
    '''
    Use bubble sort algorithm, time complexity: O(N^2)
    '''
    for i in range(len(f)):
        pivot_idx = i
        for j in range(i, len(f)):
            if f[pivot_idx] > f[j]:
                # Swap in finish list
                temp = f[pivot_idx]
                f[pivot_idx] = f[j]
                f[j] = temp
                
                # Swap in start list
                temp = s[pivot_idx]
                s[pivot_idx] = s[j]
                s[j] = temp

def iterative_acitivity_selector(s, f):
    n = len(s)
    A = [1]
    k = 1
    for m in range(2, n):
        if s[m] >= f[k]:
            A.append(m)
            k = m
                      
    return A

def test():
    # activities start with a fictitious acitivity a0 with f0 = 0
    s1 = [0,1,3,0,5,3,5,6,8,8,2,12]
    f1 = [0,4,5,6,7,9,9,10,11,12,14,16] # finish times have to be ordered in nondecreasing.
    sort_by_finish(s1, f1)
    print(recursive_activity_selector(s1, f1, 0, len(s1)))
    print(iterative_acitivity_selector(s1, f1))
    
if __name__ == '__main__':
    test()