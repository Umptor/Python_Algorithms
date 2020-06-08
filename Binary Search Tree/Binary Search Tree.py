class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BST:
    root: Node = None

    def __init__(self):
        pass

    def addNode(self, element):
        if self.root is None:
            self.root = Node(element)
            return

        current_node = self.root
        while element is not None:
            if element > current_node.value:
                if current_node.right is None:
                    current_node.right = Node(element)
                    return
                current_node = current_node.right
            else:
                if current_node.left is None:
                    current_node.left = Node(element)
                    return
                current_node = current_node.left

    def printInOrder(self):
        self.printInOrderAlgo(self.root)

    def printInOrderAlgo(self, current):
        if current.left is not None:
            self.printInOrderAlgo(current.left)
        print(current.value)
        if current.right is not None:
            self.printInOrderAlgo(current.right)


f = open('BST Array.txt', 'r')
line = f.readline().split(" ")
for j in range(len(line)):
    line[j] = int(line[j])

BST = BST()
for number in line:
    BST.addNode(number)

BST.printInOrder()
