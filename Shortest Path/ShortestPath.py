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
        for i in range(0, len(adj_matrix)):
            self.nodes.append(Node(i))

        for i in range(len(adj_matrix)):
            for j in range(len(adj_matrix)):
                if adj_matrix[i][j] is not 0:
                    self.nodes[i].addEdge((self.nodes[j], adj_matrix[i][j]))

    def shortest_route(self, start, end):
        shortest_paths = []
        for i in range(len(self.nodes)):
            shortest_paths.append([[], math.inf])
        shortest_paths[start][1] = 0
        shortest_paths[start][0] = [start]

        return self.shortest_route_algo([self.nodes[start]], shortest_paths)[end]

    def shortest_route_algo(self, current_nodes, shortest_paths):
        if len(current_nodes) == 0:
            return shortest_paths

        new_nodes = []
        for node in current_nodes:
            for edge in node.edges:
                new_distance = shortest_paths[node.value][1] + edge[1]
                if new_distance >= shortest_paths[edge[0].value][1]:
                    continue

                new_route = shortest_paths[node.value][0] + [edge[0].value]
                shortest_paths[edge[0].value][0] = new_route
                shortest_paths[edge[0].value][1] = new_distance

                new_nodes.append(edge[0])

        return self.shortest_route_algo(new_nodes, shortest_paths)


adj = []
f = open('Shortest Path Text.txt', 'r')
nodeCount = int(f.readline())
for line in range(nodeCount):
    line = f.readline().split(" ")
    for j in range(len(line)):
        line[j] = int(line[j])
    adj.append(line)

graph = Graph(adj)
print(graph.shortest_route(1, 0))

