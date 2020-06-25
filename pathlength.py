import networkx as nx

def CalculateLength(graph, nodes):
    i = 1
    length = 0
    start = nodes[0]
    try:
        while True:
            end = nodes[i]
            # graph[node] returns a dictionary of all nodes that the given node is connected to
            length += graph[start][end]["weight"]
            start = end
            i += 1
    #function returns once it reaches the end of the list of nodes
    except IndexError:
        return length
        
graph = nx.Graph()
graph.add_edge(0, 1, weight=2)
graph.add_edge(0, 2, weight=1)
graph.add_edge(1, 2, weight=2)
graph.add_edge(1, 3, weight=1)
graph.add_edge(2, 3, weight=2)
graph.add_edge(3, 0, weight=2)

#test cases
print(CalculateLength(graph, [0, 1, 2, 3, 0]))
print(CalculateLength(graph, [0, 2, 1, 3, 0]))
