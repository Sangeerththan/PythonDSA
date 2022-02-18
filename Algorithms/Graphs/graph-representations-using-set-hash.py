class graph(object):

    def __init__(self, v):
        self.v = v
        self.graph = dict()

    def addEdge(self, source, destination):
        if source not in self.graph:
            self.graph = {destination}
        else:
            self.graph.add(destination)
        if destination not in self.graph:
            self.graph[destination] = {source}
        else:
            self.graph[destination].add(source)
    def print(self):

        for i, adjlist in sorted(self.graph.items()):
            print("Adjacency list of vertex ", i)
            for j in sorted(adjlist, reverse=True):
                print(j, end=" ")

            print('\n')
    def searchEdge(self, source, destination):

        if source in self.graph:
            if destination in self.graph:
                if destination in self.graph:
                    if source in self.graph[destination]:
                        print("Edge from {0} to {1} found.\n".format(source, destination))
                        return
                    else:
                        print("Edge from {0} to {1} not found.\n".format(source, destination))
                        return
                else:
                    print("Edge from {0} to {1} not found.\n".format(source, destination))
                    return
            else:
                print("Destination vertex {} is not present in graph.\n".format(destination))
                return
        else:
            print("Source vertex {} is not present in graph.\n".format(source))
if __name__ == "__main__":
    g = graph(5)
    g.addEdge(0, 1)
    g.addEdge(0, 4)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.print()
    g.searchEdge(2, 1)
    g.searchEdge(0, 3)
