import sys
# Read input from standard input
adj_list={}

for line in sys.stdin:

    if line.startswith("#"):
        continue

    # Split the input line into a list of two elements representing the source and target vertices
    row = line.strip().split("\t")
    
    # Extract the source and target vertices from the row
    source, target = (row[0]), row[1]

    # If the source vertex isn't in the dictionary yet, add it
    if source not in adj_list:
        adj_list[source] = [target]
    else:
        adj_list[source].append(target)

    # If the target vertex isn't in the dictionary yet, add it
  #  if target not in adj_list:
  #      adj_list[target] = []
  #      adj_list[target].append(source)

    # Add the target vertex to the source vertex's list of neighbors, and vice versa
 #   if target not in adj_list[source]:
       
  #  if source not in adj_list[target]:
       

# Output the adjacency list
for source, targets in adj_list.items():
    print(f"{source}\t{' '.join(targets)}")
