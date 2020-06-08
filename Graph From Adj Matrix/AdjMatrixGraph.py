class Node:

    def __init__(self, value):
        self.children = []
        self.value = value

    def addChild(self, node):
        self.children.append(node)


class Graph:

    def __init__(self, adj_matrix):
        self.nodes = []
        for i in range(0, len(adj_matrix)):
            self.nodes.append(Node(i))

        for i in range(len(adj_matrix)):
            for j in range(len(adj_matrix)):
                if adj_matrix[i][j] is not 0:
                    self.nodes[i].addChild((self.nodes[j], adj_matrix[i][j]))

    def printNodes(self):
        for node in self.nodes:
            for i in range(len(node.children)):
                print(f"{node.children[i][0].value} {node.children[i][1]}  ", end="")
            print("")



adj = []
f = open('AdjMatrixGraph.txt', 'r')
nodeCount = int(f.readline())
for line in range(nodeCount):
    line = f.readline().split(" ")
    for j in range(len(line)):
        line[j] = int(line[j])
    adj.append(line)

graph = Graph(adj)
graph.printNodes()
