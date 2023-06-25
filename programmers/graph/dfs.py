class Node:
    def __init__(self, _name: str):
        self.name = _name
        self.color = None
        self.parent = None
        self.startTime = 0
        self.finishTime = 0
        
class Graph:
    def __init__(self):
        self.V = []
        self.E = []
        self.depth = float('inf')

    def Adj(self, _u: Node):
        adj = []
        for u, v in self.E:
            if u == _u:
                adj.append(v)
            # elif v == _u:
            #     adj.append(u)
            else:
                continue
        return adj
    
    def addVertex(self, u: Node):
        self.V.append(u)
    
    def addEdge(self, u: Node, v: Node):
        self.E.append((u, v))
    
    def printGraph(self):
        print('**Graph information**')
        print('Vertices: ', end=' ')
        for v in self.V:
            print(v.name, end=' ')
        
        print('\nEdges: ', end=' ')
        for u, v in self.E:
            print(f'({u.name}, {v.name})', end=' ')
        print()
        
def dfs(G: Graph):
    '''
    DFS: Depth First Search
    Input:
        G: a graph
        s: a start node
    Total running time: O(V+E)
    '''
    # Initialize nodes
    for u in G.V:
        u.color = 'WHITE'
        u.parent = 'NIL'
    global time
    time = 0
    for u in G.V:
        if u.color == 'WHITE':
            dfsVisit(G, u)
            
def dfsVisit(G: Graph, u: Node):
    global time
    time += 1
    u.startTime = time
    u.color = 'GRAY'
    for v in G.Adj(u):
        if v.color == 'WHITE':
            v.parent = u
            dfsVisit(G, v)
    u.color = 'BLACK'
    time += 1
    u.finishTime = time

def test():
    # Initialize each node for constructing a graph
    u, v, w, x, y, z = Node('u'), Node('v'), Node('w'), Node('x'), Node('y'), Node('z')
    Nodes = [u, v, w, x, y, z]
    Edges = [(u, v), (u, x), (v, y), (w, y), (w, z), (x, y), (y, x), (z, z)]
    
    # Initialize a graph and add vertices & edges
    G = Graph()
    for i in Nodes:
        G.addVertex(i)
    for i, j in Edges:
        G.addEdge(i, j)
    
    # Show the graph
    G.printGraph()
    
    # BFS
    dfs(G)
    
    # Show the graph after dfs
    print('\n**Graph after DFS -> Node:((startTime/finishTime), parent)**')
    for v in G.V:
        if v.parent != 'NIL':
            print(f'{v.name}:({v.startTime}/{v.finishTime}, {v.parent.name})', end=' ')
        else:
            print(f'{v.name}:({v.startTime}/{v.finishTime}, NIL)', end=' ')
    print()
           
if __name__ == '__main__':
    test()