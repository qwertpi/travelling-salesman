from copy import copy
from math import inf
from random import choice, randint
##from time import sleep
import networkx as nx


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

graph = nx.Graph()
#creates a random graph
#this can be changed easily
number_of_nodes = 20
for i in range(0, number_of_nodes):
    for j in range(i, number_of_nodes):
        graph.add_edge(i, j, weight=randint(1, 20))


nodes = list(graph.nodes())
best_cycle = []
best_cycle_len = inf

try:
    while True:
        cycle = []
        #while there is not a full cycle
        while len(cycle) < len(nodes):
            #picks a random node
            pick = choice(nodes)
            #only adds the random node to the cycle if it isn't already in the cycle
            if pick not in cycle:
                cycle.append(pick)
                
        #closes the cycle by returning to start
        cycle.append(cycle[0])
        #calculates total weight of cycle
        length = CalculateLength(graph, cycle)
        ##print(f"Trying {cycle} with weight {length}")
        
        if best_cycle_len > length:
            best_cycle = copy(cycle)
            best_cycle_len = length
            print(f"Best cycle is {best_cycle} with weight {best_cycle_len}")
        ##sleep(0.25)
except KeyboardInterrupt:
    print(f"Best cycle is {best_cycle} with weight {best_cycle_len}")

