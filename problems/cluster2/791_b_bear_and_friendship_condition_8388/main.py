#!/usr/bin/env python3

from library import Graph

n, m = map(int, input().split())
graph = Graph(n + 1)  # 1-indexed

for _ in range(m):
    a, b = map(int, input().split())
    graph.add_edge(a, b)

visited = {}

def check_friendship_condition(start_node):
    """
    Check if a connected component satisfies the friendship condition:
    Each component should be a complete graph (all nodes connected to all other nodes)
    """
    component_nodes = []
    queue = [start_node]
    local_visited = {start_node: True}
    component_nodes.append(start_node)
    
    # BFS to find all nodes in the component
    while queue:
        node = queue.pop(0)
        neighbors = graph.neighbors(node)
        
        for neighbor in neighbors:
            if neighbor not in local_visited:
                local_visited[neighbor] = True
                queue.append(neighbor)
                component_nodes.append(neighbor)
    
    # Count edges in the component
    edge_count = 0
    for node in component_nodes:
        edge_count += len(graph.neighbors(node))
    
    # Each edge is counted twice (once from each end)
    edge_count //= 2
    
    # For a complete graph with k nodes, there should be k*(k-1)/2 edges
    component_size = len(component_nodes)
    expected_edges = (component_size * (component_size - 1)) // 2
    
    return edge_count == expected_edges

# Check each connected component
result = "Yes"  # Match the case in the expected output

for i in range(1, n + 1):
    if i not in visited:
        # Check if this component satisfies the friendship condition
        if not check_friendship_condition(i):
            result = "No"  # Match the case in the expected output
            break
        
        # Add all nodes in this component to visited
        stack = [i]
        visited[i] = True
        
        while stack:
            node = stack.pop()
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    visited[neighbor] = True
                    stack.append(neighbor)

print(result)