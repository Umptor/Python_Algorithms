import math


class Node:
    def __init__(self, value):
        self.edges = []
        self.value = value

    def addEdge(self, node):
        self.edges.append(node)


class Graph:
    def __init__(self, adj_matrix):
        self.nodes = []
        self.bellman_ford_distances = []
        for i in range(0, len(adj_matrix)):
            self.nodes.append(Node(i))
            self.bellman_ford_distances.append(math.inf)

        for i in range(len(adj_matrix)):
            for j in range(len(adj_matrix)):
                if adj_matrix[i][j] is not 0:
                    self.nodes[i].addEdge((self.nodes[j], adj_matrix[i][j]))


def bellman_ford(start, graph: Graph):
    graph.bellman_ford_distances[start] = 0
    for i in range(len(graph.nodes) - 1):
        for node in graph.nodes:
            for edge in node.edges:
                new_distance = graph.bellman_ford_distances[node.value] + edge[1]

                if new_distance < graph.bellman_ford_distances[edge[0].value]:
                    graph.bellman_ford_distances[edge[0].value] = new_distance

    for i in range(len(graph.nodes) - 1):
        for node in graph.nodes:
            for edge in node.edges:
                new_distance = graph.bellman_ford_distances[node.value] + edge[1]

                if new_distance < graph.bellman_ford_distances[edge[0].value]:
                    graph.bellman_ford_distances[edge[0].value] = -math.inf

    return graph.bellman_ford_distances


adj = []
f = open('Bellman Ford.txt', 'r')
nodeCount = int(f.readline())
for line in range(nodeCount):
    line = f.readline().split(" ")
    for j in range(len(line)):
        line[j] = int(line[j])
    adj.append(line)

graph = Graph(adj)
print(bellman_ford(0, graph))
