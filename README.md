# Shortest-Path-Analysis-on-Large-Graphs-using-Hadoop
This repository contains two Python scripts and one Jupyter Notebook:

## BFS-Large-Graphs.ipynb:
This notebook is the simple implementation of the BFS on very large size graph of 4.3 Million Nodes. We used this to compare the efficieny of the algorithim if we run it as a Map Reduce Job of Apache Hadoop.

## create_adjacency_list.py:
This script reads a graph from standard input and outputs its adjacency list. The graph should be represented as a list of edges, where each edge is represented as a pair of vertices separated by a tab character. The script assumes that the first vertex of each edge is the source and the second vertex is the target. The adjacency list is represented as a dictionary, where the keys are the vertices and the values are lists of their neighbors. The script outputs the adjacency list to standard output, with each line containing a vertex and its neighbors separated by spaces.

## bfs_shortest_paths.py: 
This script reads a graph from standard input and performs a breadth-first search (BFS) starting from a given vertex. The graph should be represented as a list of edges, where each edge is represented as a pair of vertices separated by a space character. The script assumes that the first vertex of each edge is the source and the second vertex is the target. The BFS starts from a given vertex, specified as a command-line argument. The script outputs the shortest paths from the starting vertex to all other vertices reachable from it, as a sequence of vertex IDs separated by arrows, one per line.

# Usage:

To use these scripts, you should have Python 3 installed on your machine. You can run the scripts from the command line, as follows:

### create_adjacency_list.py:
To create the adjacency list of a graph, you can run the script and pipe the input graph to it, as follows:

`$ cat input_graph.txt | python bfs_shortest_paths.py 847`

This will read the input graph from the input_graph.txt file, create its adjacency list, and output it to the adjacency_list.txt file.

## bfs_shortest_paths.py:
To compute the shortest paths from a given vertex in a graph, you can run the script and pass the starting vertex ID as a command-line argument, as follows:

`$ cat input_graph.txt | python bfs_shortest_paths.py 847`

This will read the input graph from the input_graph.txt file, perform a BFS starting from vertex 847, and output the shortest paths to all other vertices reachable from it to the standard output.

## Hadoop Map-Reduce

Overall implementation is focused on hadoop for big data problems using Map-Reduce. You can run it using:

`$ hadoop jar path/to/streamingfile -file path/to/mapper.py -mapper 'python3 mapper.py' -file path/to/reducer.py -reducer 'python3 reducer.py' -input /path/to input file in hdfs/input.txt -output path/to outputfile in hdfs/output`

This step follows after uploading the concerned files on hdfs.
