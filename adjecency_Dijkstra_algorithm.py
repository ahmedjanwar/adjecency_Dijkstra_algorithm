#Generate adjacency lists of 10 nodes as the following figure. 
# Write a Python function which converts the adjacency lists into adjacency matrix. 
# Apply Dijkstra algorithm for the adjacency matrix and output the shortest distance from Node 𝑋
# to all other nodes, where 𝑋
#='A'+lastDigitofYourID. E.g., if your ID is e2301234 then your program outputs Node 𝐸's result.

import random
import numpy as np
import heapq

# using my student number as the seed for randomness
# example 2001332
student_number = int(input("Enter your student number (Numbers only): "))
random.seed(student_number)

def generate_adjacency_lists(num_nodes):
    adj_lists = [[] for _ in range(num_nodes)]
    return adj_lists

def add_edge(adj_lists, u, v, weight):
    adj_lists[u].append((v, weight))
    adj_lists[v].append((u, weight))  # For undirected graph

def adjacency_lists_to_matrix(adj_lists):
    num_nodes = len(adj_lists)
    adj_matrix = np.inf * np.ones((num_nodes, num_nodes))
    
    for u, edges in enumerate(adj_lists):
        for v, weight in edges:
            adj_matrix[u][v] = weight
    
    np.fill_diagonal(adj_matrix, 0)
    return adj_matrix

def dijkstra(adj_matrix, start):
    num_nodes = len(adj_matrix)
    distances = np.inf * np.ones(num_nodes)
    visited = [False] * num_nodes
    distances[start] = 0
    
    min_heap = [(0, start)]
    
    while min_heap:
        current_distance, u = heapq.heappop(min_heap)
        
        if visited[u]:
            continue
        
        visited[u] = True
        
        for v in range(num_nodes):
            if not visited[v] and adj_matrix[u][v] != np.inf:
                alt = current_distance + adj_matrix[u][v]
                
                if alt < distances[v]:
                    distances[v] = alt
                    heapq.heappush(min_heap, (alt, v))
    
    return distances

# Example usage
num_nodes = 11  # to fix indexing since we have 1-10 nodes
adj_lists = generate_adjacency_lists(num_nodes)

# Add edges based on your graph
add_edge(adj_lists, 0, 1, 3)  # A to B
add_edge(adj_lists, 1, 7, 1)  # B to H
add_edge(adj_lists, 0, 6, 3)  # A to G
add_edge(adj_lists, 0, 3, 7)  # A to D
add_edge(adj_lists, 7, 6, 1)  # H to G
add_edge(adj_lists, 3, 2, 1)  # D to C
add_edge(adj_lists, 3, 9, 3)  # D to S
add_edge(adj_lists, 2, 8, 8)  # C to G
add_edge(adj_lists, 8, 9, 9)  # C to S
add_edge(adj_lists, 6, 9, 4)  # G to S
add_edge(adj_lists, 3, 4, 2)  # D to E
add_edge(adj_lists, 4, 5, 6)  # E to F
add_edge(adj_lists, 9, 10, 2)  # S to T
add_edge(adj_lists, 4, 10, 1)  # E to T

# Convert adjacency lists to adjacency matrix
adj_matrix = adjacency_lists_to_matrix(adj_lists)

# Calculate the last digit of your student number
last_digit_of_id = student_number % 10

# Calculate the start node based on the last digit of your student number
start_node = last_digit_of_id

# Find shortest distances from the start node
shortest_distances = dijkstra(adj_matrix, start_node)

# Output shortest distances
for i, distance in enumerate(shortest_distances):
    if i != start_node:
        if i != start_node and chr(i + ord('A')) != 'I':  # Skip Node I
            if(i == 9):
                print(f"Shortest distance from Node {chr(start_node + ord('A'))} to Node S: {distance}")
            elif(i == 10):
                print(f"Shortest distance from Node {chr(start_node + ord('A'))} to Node T: {distance}")
            else:
                print(f"Shortest distance from Node {chr(start_node + ord('A'))} to Node {chr(i + ord('A'))}: {distance}")
            #print(i)
