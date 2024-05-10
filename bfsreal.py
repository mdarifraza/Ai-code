from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            v = queue.popleft()
            print(v, end=' ')
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

# Taking input from the user
g = Graph()
edges = int(input("Enter the number of edges: "))

for _ in range(edges):
    u, v = input("Enter two vertices (u v): ").split()
    g.add_edge(u, v)

start_node = input("Enter the starting node for BFS: ")
print("Breadth First Traversal from node {}:".format(start_node))
print("Total Number Edges = " , edges)
print("\n")
print("Total numbers of Vertices = " , edges-1)
print("\n")
print("Starting node =" ,start_node)
print("\n")
print("BFS traversing  = ")
g.bfs(start_node)
