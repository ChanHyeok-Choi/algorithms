def rod_cut(p, n):
    '''
    Top-down and recursive implementation
    Time complexity: O(2^N)
    '''
    if n == 0:
        return 0
    q = float('-inf') # -inf
    for i in range(n):
        q = max(q, p[i] + rod_cut(p, n-i-1))
    
    return q

def memoized_rod_cut(p, n):
    '''
    Top-down with memoization
    '''
    r = []
    for i in range(n+1):
        r.append(float('-inf'))
    return memoized_rod_cut_aux(p, n, r)


def memoized_rod_cut_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float('-inf')
        for i in range(n):
            q = max(q, p[i] + memoized_rod_cut_aux(p, n-i-1, r))
        r[n] = q
    return q

def bottom_up_rod_cut(p, n):
    '''
    Bottum-up with memoization
    '''
    r = [float('-inf')] * n
    r.insert(0, 0)  # r[0] = 0
    for i in range(1, n+1):
        q = float('-inf')
        for j in range(1, i+1):
            q = max(q, p[j] + r[i-j])
        r[i] = q
    return r[n]

def test():
    p1 = [1,5,8,9,10,17,17,20,24,30]
    print("Recursive rod cut")
    for i in range(len(p1)):
        print(i+1, ": ", rod_cut(p1, i+1))
    
    p1 = [1,5,8,9,10,17,17,20,24,30]
    print()
    print("Top-down memoization rod cut")
    for i in range(len(p1)):
        print(i+1, ": ", memoized_rod_cut(p1, i+1))
        
    p1 = [0,1,5,8,9,10,17,17,20,24,30]
    print()
    print("Bottom-up memoization rod cut")
    for i in range(len(p1)-1):
        print(i+1, ": ", bottom_up_rod_cut(p1, i+1))
    
if __name__ == '__main__':
    test()