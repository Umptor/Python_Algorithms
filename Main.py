adj = []




def startDfs(start, find, nodeCount):
    visited = [False] * nodeCount
    visited[start] = True

    def dfs(start, find):
        for i in range(len(adj[start])):
            nextNode = adj[start][i]
            if nextNode == find:
                return [find]

            if visited[nextNode]:
                continue

            visited[int(nextNode)] = True
            route = dfs(nextNode, find)
            if route[-1:][0] == find:
                route.insert(0, nextNode)
                return route

        return [False]

    route = dfs(start, find)
    if route == [False]:
        return route
    route.insert(0, start)
    return route




nodeCount = int(input())

for i in range(nodeCount):
    row = adj.append([])

for i in range(nodeCount):
    row = input().split(" ")
    for j in range(len(row)):
        row[j] = int(row[j])

    first = int(row[0])
    row.pop(0)
    row.sort()
    adj[first] = row

print(adj)

print(startDfs(int(input()), int(input()), nodeCount))



# nodeCount
# firstNode other nodes
# ...

