from collections import deque
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = [[] for _ in range(n)]
        in_degree = [0] * n

        # Build the reverse graph and calculate in-degrees
        for i in range(n):
            for neighbor in graph[i]:
                reverse_graph[neighbor].append(i)
            in_degree[i] = len(graph[i])

        # Start with terminal nodes (nodes with 0 out-degree)
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        safe_nodes = []

        # Process nodes in topological order
        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for neighbor in reverse_graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Return the sorted list of safe nodes
        return sorted(safe_nodes)
