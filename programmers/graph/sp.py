class Node:
    def __init__(self, _name: str):
        self.name = _name
        self.d = float('inf')
        self.parent = 'NIL'
        
class Graph:
    def __init__(self):
        self.V = []
        self.E = []
    
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
    
    def printPath(self):
        for v in self.V:
            if v.parent != 'NIL':
                print(f'({v.name}, {v.d}, {v.parent.name})', end=' ')
            else:
                print(f'({v.name}, {v.d}, NIL)', end=' ')
        print()
        
def sp(G: Graph, s: Node, type: str):
    '''
    SP: Shortest Path
    Input:
        G: a graph
        s: a starting node
        type: What type for mst, e.g., Bellman-Ford or Dijkstra
    Total running time: O(ElogV)
    '''
    if type == 'bellman-ford':
        return bellman_ford(G, s)
    elif type == 'dijkstra':
        return dijkstra(G, s)

def initializeSingleSource(G: Graph, s: Node):
    for v in G.V:
        v.d = float('inf')
        v.parent = 'NIL'
    s.d = 0

def relax(u: Node, v: Node, G: Graph):
    if v.d > u.d + G.Weight(u, v):
        v.d = u.d + G.Weight(u, v)
        v.parent = u
        
def bellman_ford(G: Graph, s: Node):
    '''
    Input:
        G: a graph
        s: a starting node
    Output: if there exists a shortest path, True, otherwise, False
    '''
    initializeSingleSource(G, s)
    for i in range(len(G.V)-1):
        for u, v, w in G.E:
            relax(u, v, G)
    for u, v, w in G.E:
        if v.d > u.d + G.Weight(u, v):
            return False
    return True

def dijkstra(G: Graph, s: Node):
    '''
    Input:
        G: a graph
        s: a starting node
    Output: a shortest path set
    '''
    initializeSingleSource(G, s)
    S = []
    Q = G.V.copy()
    sorted(Q, key=lambda x: x.d)
    while Q:
        sorted(Q, key=lambda x: x.d)
        u = Q.pop(0)
        S = S + [u]
        for v in G.Adj(u):
            relax(u, v, G)
    return S

def test():
    # Initialize each node for constructing a graph
    s, t, x, y, z = Node('s'), Node('t'), Node('x'), Node('y'), Node('z')
    Nodes = [s, t, x, y, z]
    Edges = [(s, t, 6), (s, y, 7), (t, x, 5), (t, y, 8), 
             (t, z, -4), (x, t, -2), (y, x, -3), (y, z, 9),
             (z, s, 2), (z, x, 7)]
    
    # Initialize a graph and add vertices & edges
    G = Graph()
    for i in Nodes:
        G.addVertex(i)
    for i, j, k in Edges:
        G.addEdge(i, j, k)
    
    # Show the graph
    G.printGraph()
    
    # Bellman-Ford's algorithm
    print('\n**SP by Bellman-Ford\'s algorithm**')
    print(sp(G, G.V[0], 'bellman-ford'))
    G.printPath()
    
    ######################################################################
    # Initialize each node for constructing a graph
    s, t, x, y, z = Node('s'), Node('t'), Node('x'), Node('y'), Node('z')
    Nodes = [s, t, x, y, z]
    Edges = [(s, t, 10), (s, y, 5), (t, x, 1), (t, y, 2), 
             (x, z, 4), (y, t, 3), (y, x, 9), (y, z, 2),
             (z, s, 7), (z, x, 6)]
    
    # Initialize a graph and add vertices & edges
    G = Graph()
    for i in Nodes:
        G.addVertex(i)
    for i, j, k in Edges:
        G.addEdge(i, j, k)
    
    # Dijkstra's algorithm
    print('\n**SP by Dijkstra\'s algorithm**')
    S = sp(G, G.V[0], 'dijkstra')
    for i in S:
        if i.parent != 'NIL':
            print(f'({i.name}, {i.d}, {i.parent.name})', end=' ')
        else:
            print(f'({i.name}, {i.d}, NIL)', end=' ')
    print()
    
           
if __name__ == '__main__':
    test()