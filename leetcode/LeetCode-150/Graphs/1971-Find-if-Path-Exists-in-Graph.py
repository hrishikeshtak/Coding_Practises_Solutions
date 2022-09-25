"""
1971. Find if Path Exists in Graph
"""

from typing import List
from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        # prepare adj list repr of edges
        adj_list = defaultdict(set)
        for edge in edges:
            adj_list[edge[0]].add(edge[1])
            adj_list[edge[1]].add(edge[0])
        q = []
        visited = [False] * n
        q.append(source)
        visited[source] = True
        while q:
            cur = q.pop(0)
            for node in adj_list[cur]:
                if not visited[node]:
                    q.append(node)
                    visited[node] = True
        return visited[destination]
