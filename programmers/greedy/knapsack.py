def knapsack01(C, n):
    '''
    Greedy method cannot solve 0-1 knapsack problem, so check whether it can be resolved by dp.
    * Principle of Optimality:
        It is said to be applicable to a problem if an optimal solution to an instance of a problem always contains optimal solutions to all substances.
    Input:
        C: total capacity
        n: tuple list of weights and values
    '''
    # Declare 2D array
    k = [[0 for j in range(C+1)] for i in range(len(n)+1)]
    for i, (weight, value) in enumerate(n):
        for j in range(C+1):
            if weight > j:
                k[i+1][j] = k[i][j]
            else:
                k[i+1][j] = max(k[i][j], k[i][j-weight] + value)
    
    return k

def fractinoal_knapsack(C, n):
    '''
    Greedy method can be applicable to fractinoal knapsack problem.
    Input:
        C: total capacity
        n: tuple list of weights and values
    '''
    current_weight = 0
    final_value = 0
    for i, (weight, value) in enumerate(n):
        if weight + current_weight <= C:
            current_weight += weight
            final_value += value
        else:
            remain = C - current_weight
            final_value += remain * (value / weight)
    return final_value

def test():
    # activities start with a fictitious acitivity a0 with f0 = 0
    items = [(10,60),(20,100),(30,120)]
    print("0-1 knapsack problem solved by dynamic programming")
    print(*knapsack01(50, items), sep='\n')
    
    print("\nFractional knapsack problem soloved by greedy algorithm")
    print(fractinoal_knapsack(50, items))
    
    
if __name__ == '__main__':
    test()