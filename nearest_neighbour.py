import networkx as nx
from random import randint, shuffle

graph = nx.Graph()
graph.add_edge(0, 1, weight=randint(1,20))
graph.add_edge(0, 2, weight=randint(1,20))
graph.add_edge(0, 3, weight=randint(1,20))
graph.add_edge(0, 4, weight=randint(1,20))
graph.add_edge(0, 5, weight=randint(1,20))
graph.add_edge(0, 6, weight=randint(1,20))
graph.add_edge(1, 2, weight=randint(1,20))
graph.add_edge(1, 3, weight=randint(1,20))
graph.add_edge(1, 4, weight=randint(1,20))
graph.add_edge(1, 5, weight=randint(1,20))
graph.add_edge(1, 6, weight=randint(1,20))
graph.add_edge(2, 3, weight=randint(1,20))
graph.add_edge(2, 4, weight=randint(1,20))
graph.add_edge(2, 5, weight=randint(1,20))
graph.add_edge(2, 6, weight=randint(1,20))
graph.add_edge(3, 4, weight=randint(1,20))
graph.add_edge(3, 5, weight=randint(1,20))
graph.add_edge(3, 6, weight=randint(1,20))
graph.add_edge(4, 5, weight=randint(1,20))
graph.add_edge(4, 6, weight=randint(1,20))
graph.add_edge(5, 6, weight=randint(1,20))

def CalculateLength(graph, nodes):
    i = 1
    length = 0
    start = nodes[0]
    try:
        while True:
            end = nodes[i]
            length += graph[start][end]["weight"]
            start = end
            i += 1
    except IndexError:
        return length
    except:
        print(start, end)

shuffled_nodes = list(graph.nodes())
shuffle(shuffled_nodes)
for start_node in shuffled_nodes:
    nodes = list(graph.nodes())
    num_nodes = len(nodes)
    cycle = [start_node]
    nodes.remove(start_node)
    while len(cycle) < num_nodes:
        prev_node = cycle[-1]
        distances = {graph[prev_node][node]["weight"]:node for node in nodes if node != prev_node}
        best_node = distances[min(distances.keys())]
        nodes.remove(best_node)
        cycle.append(best_node)
    #closes the cycle
    cycle.append(start_node)
    length = CalculateLength(graph, cycle)
    print(f"Produced {cycle} with length {length} from starting node {start_node}")
    print(graph)