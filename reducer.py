#!/usr/bin/env python

import sys
import csv



def bfs_reduce(graph, start):
    queue = [(start, [start], 0)] # [(StartingNode,[Path of Starting Node],Cost/Length of Starting Node)]
    front = 0 # Pointer Front
    rear = 1 # Pointer Back
    visited = set([start]) 
    paths = {start: [start]} # Dictionary Maintaing Paths from StartNode(709) to every other node
    path_lengths = {start: 0} # Lengths of Path
    while front < rear: # Until List is not empty
    	node, path, length = queue[front] #1,[1],0 for the first ietration
    	front += 1 # Moving the pointer to the next element in the queue/list
    	if node in graph.keys():
            for neighbor in graph[node]: # We will use this loop to traverse all the neighbours and add them to the list
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_length = length + 1 # Increase the length by 1 because we have covered distance of one 709-->n1
                    if neighbor not in path_lengths or new_length < path_lengths[neighbor]:
                        path_lengths[neighbor] = new_length
                        paths[neighbor] = path + [neighbor]
                        queue.append((neighbor, path + [neighbor], new_length))
                        rear += 1



#    with open(f'{start}_shortest_paths.csv', 'w') as csvfile:
#        writer = csv.writer(csvfile)
#        for target in paths:
#            if target != start:
#                writer.writerow([start, target, ','.join(str(x) for x in paths[target])])
#    print(f'Shortest paths written to {start}_shortest_paths.csv')

    for target in paths:
        if target != start:
            print(f'Shortest path from {start} to {target}: {" -> ".join(str(x) for x in paths[target])}')

if __name__ == '__main__':
    # Initialize the adjacency list dictionary
    adj_list = {}

# Iterate over the lines of the standard input
    for line in sys.stdin:
    # Strip any whitespace from the line and split it into a list of vertices
        vertices = line.strip().split()

    # The first vertex is the key, and the remaining vertices are the neighbors
        key = vertices[0]
        neighbors = vertices[1:]

    # Add the key and neighbors to the adjacency list dictionary
        adj_list[key] = neighbors

    bfs_reduce(adj_list,'847')



