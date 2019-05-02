from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def get_neighbours(self, u):
        return self.graph[u]



""" Driver code """

graph = Graph()
graph.add_edge('Ram', 'Sham')
graph.add_edge('Ghansham', 'Jyoti')
graph.add_edge('Ram', 'Ghansham')
graph.add_edge('Sham', 'Jyoti')

print(graph.graph)

for person in graph.graph:
    print(person + ' is connected with', end='\t')
    print(graph.get_neighbours(person))
