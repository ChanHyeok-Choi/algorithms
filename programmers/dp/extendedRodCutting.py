def extended_bottom_up_rod_cut(p, n):
    '''
    Extended bottum-up with memoization
    '''
    r = [0] * (n+1)
    s = [0] * (n+1)
    for i in range(1, n+1):
        q = float('-inf')
        for j in range(1, i+1):
            if q < p[j] + r[i-j]:
                q = p[j] + r[i-j]
                s[i] = j
        r[i] = q
    return r, s

def print_cut_rod_solution(p, n):
    r, s = extended_bottom_up_rod_cut(p, n)
    while n > 0:
        print(s[n], end=' ')
        n -= s[n]  

def test():
    p1 = [0,1,5,8,9,10,17,17,20,24,30]
    print("Bottom-up memoization rod cut")
    for i in range(len(p1)-1):
        print(i+1, ": ", extended_bottom_up_rod_cut(p1, i+1))
    
    print()
    print("Print cut rod solution")
    for i in range(len(p1)-1):
        print_cut_rod_solution(p1, i+1)
    print()
    
if __name__ == '__main__':
    test()