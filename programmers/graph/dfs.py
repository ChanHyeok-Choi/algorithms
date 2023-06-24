class Node:
    def __init__(self, _name: str):
        self.name = _name
        self.color = None
        self.d = 0
        self.parent = None
        
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
            elif v == _u:
                adj.append(u)
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
        
def dfs(G: Graph, s: Node):
    '''
    DFS: Depth First Search
    Input:
        G: a graph
        s: a start node
    Total running time: O(V+E)
    '''
        

def test():
    # Initialize each node for constructing a graph
    r, s, t, u, v, w, x, y = Node('r'), Node('s'), Node('t'), Node('u'), Node('v'), Node('w'), Node('x'), Node('y')
    Nodes = [r, s, t, u, v, w, x, y]
    Edges = [(r, s), (r, v), (s, w), (t, w), (t, u), (t, x), (u, y), (u, x), (w, x), (x, y)]
    
    # Initialize a graph and add vertices & edges
    G = Graph()
    for u in Nodes:
        G.addVertex(u)
    for u, v in Edges:
        G.addEdge(u, v)
    
    # Show the graph
    G.printGraph()
    
    # BFS
    dfs(G, s)
    
    # Show the graph after bfs
    print('\n**Graph after BFS -> Node:(depth, parent)**')
    for v in G.V:
        if v.parent != 'NIL':
            print(f'{v.name}:({v.d}, {v.parent.name})', end=' ')
        else:
            print(f'{v.name}:({v.d}, NIL)', end=' ')
    print()
           
if __name__ == '__main__':
    test()