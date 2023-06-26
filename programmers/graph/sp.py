class Node:
    def __init__(self, _name: str):
        self.name = _name
        self.key = float('inf')
        self.parent = 'NIL'
        
class Graph:
    def __init__(self):
        self.V = []
        self.E = []
        self.S = []
        
    def MakeSet(self, v: Node):
        self.S.append([v])
    
    def FindSet(self, u: Node):
        for s in self.S:
            for v in s:
                if u == v:
                    # print(f'{u.name}:', end=' ')
                    # for i in s:
                    #     print(f'{i.name}', end=' ')
                    # print()
                    return sorted(s, key=lambda x: x.name)
        # Not found
        print('\033[95m' + f'Error: there is no such set w.r.t. {u.name}' + '\033[0m')
    
    def Union(self, u: Node, v: Node):
        U = []
        V = []
        while not U or not V:
            for s in self.S:
                for e in s:
                    if e == u:
                        U = self.S.pop(self.S.index(s))
                    elif e == v:
                        V = self.S.pop(self.S.index(s))
                    
        self.S.append(U + V)
    
    def Weight(self, _u: Node, _v: Node):
        for u, v, w in self.E:
            if u == _u and v == _v:
                return w
            elif u == _v and v == _u:
                return w
        return float('inf')

    def Adj(self, _u: Node):
        adj = []
        for u, v, _ in self.E:
            if u == _u:
                adj.append(v)
            # elif v == _u:
            #     adj.append(u)
            else:
                continue
        return adj
    
    def addVertex(self, u: Node):
        self.V.append(u)
    
    def addEdge(self, u: Node, v: Node, w):
        self.E.append((u, v, w))
    
    def printGraph(self):
        print('**Graph information**')
        print('Vertices: ', end=' ')
        for v in self.V:
            print(v.name, end=' ')
        
        print('\nEdges: ', end=' ')
        for u, v, w in self.E:
            print(f'({u.name}, {v.name}, {w})', end=' ')
        print()
    
    def printSet(self):
        print('Set:', end=' ')
        for s in self.S:
            for e in s:
                print(f'{e.name}', end=' ')
        print()
        
def sp(G: Graph, r: Node, type: str):
    '''
    SP: Shortest Path
    Input:
        G: a graph
        w:
        type: What type for mst, e.g., Kruscal or Prim
    Total running time: O(ElogV)
    '''
    if type == 'kruscal':
        return kruscal(G)
    elif type == 'prim':
        prim(G, r)
        
def kruscal(G: Graph):
    A = []
    for v in G.V:
        G.MakeSet(v)
    # Sort the edges of G.E into nondecreasing order by weight
    G.E = sorted(G.E, key=lambda x: x[2]) # O(NlogN)
    for u, v, w in G.E:
        if G.FindSet(u) != G.FindSet(v):
            A = A + [(u, v, w)]
            G.Union(u, v)
    return A

def prim(G: Graph, r: Node):
    '''
    Prim's algorithm uses a greedy method: chooses a local optimum each time, then leads to a global optimum
    '''
    # Initialize each node
    for u in G.V:
        u.key = float('inf')
        u.parent = 'NIL'
    r.key = 0
    Q = G.V.copy()
    sorted(Q, key=lambda x: x.key) # min-priority queue Q
    while Q:
        sorted(Q, key=lambda x: x.key)
        u = Q.pop(0) # EXTRACT-MIN-QUEUE
        for v in G.Adj(u):
            if v in Q and G.Weight(u, v) < v.key:
                v.parent = u
                v.key = G.Weight(u, v)

def test():
    # Initialize each node for constructing a graph
    a, b, c, d, e, f, g, h, i = Node('a'), Node('b'), Node('c'), Node('d'), Node('e'), Node('f'), Node('g'), Node('h'), Node('i')
    Nodes = [a, b, c, d, e, f, g, h, i]
    Edges = [(a, b, 4), (a, h, 8), (b, c, 8), (b, h, 11),
             (c, d, 7), (c, f, 4), (c, i, 2), (d, e, 9),
             (d, f, 14), (e, f, 10), (f, g, 2), (g, h, 1),
             (g, i, 6), (h, i, 7)]
    
    # Initialize a graph and add vertices & edges
    G = Graph()
    for i in Nodes:
        G.addVertex(i)
    for i, j, k in Edges:
        G.addEdge(i, j, k)
    
    # Show the graph
    G.printGraph()
    
    # Kruscal's algorithm
    print('\n**MST by Kruscal\'s algorithm**')
    A = mst(G, None, 'kruscal')
    for i, j, k in A:
        print(f'({i.name}, {j.name}, {k})', end=' ')
    
    # Prim's algorithm
    print('\n\n**MST by Prim\'s algorithm**')
    mst(G, G.V[0], 'prim')
    for i in G.V:
        if i.parent != 'NIL':
            print(f'({i.name}, {i.key}, {i.parent.name})', end=' ')
        else:
            print(f'({i.name}, {i.key}, NIL)', end=' ')
    print()
    
           
if __name__ == '__main__':
    test()