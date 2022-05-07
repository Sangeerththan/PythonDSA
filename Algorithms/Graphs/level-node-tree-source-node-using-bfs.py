import queue


def printLevels(graph, V, x):
    level = [None] * V
    marked = [False] * V
    que = queue.Queue()
    que.put(x)
    level[x] = 0
    marked[x] = True
    while (not que.empty()):
        x = que.get()
        for i in range(len(graph[x])):
            b = graph[x][i]
            if (not marked[b]):
                que.put(b)
                level[b] = level[x] + 1
                marked[b] = True
    print("Nodes", " ", "Level")
    for i in range(V):
        print(" ", i, " --> ", level[i])


# Driver Code
if __name__ == '__main__':
    V = 8
    graph = [[] for i in range(V)]

    graph[0].append(1)
    graph[0].append(2)
    graph[1].append(3)
    graph[1].append(4)
    graph[1].append(5)
    graph[2].append(5)
    graph[2].append(6)
    graph[6].append(7)
    printLevels(graph, V, 0)
