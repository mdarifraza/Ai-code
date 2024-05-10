class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self , u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)
        self.graph[u].append(v)
    def Dfs_util(self,v,visited):
            visited.add(v)  
            print(v, end=' ')
            for neioubour_node in self.graph[v]:
                if neioubour_node not in visited:
                    self.Dfs_util(neioubour_node ,visited)
                    
    def dfs(self , start):
        visited = set()
        self.Dfs_util(start , visited)
        
g = Graph()
edges  =  int(input("Enter number of edges here : "))
for _ in range(edges):
    u,v = input("Enter the two vertices(u,v)").split()
    g.add_edge(u,v)
start_node =  input("Enter the starting node of Tree :")
g.dfs(start_node)