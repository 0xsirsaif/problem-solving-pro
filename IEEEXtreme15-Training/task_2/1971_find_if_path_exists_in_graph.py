"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
The edges in the graph are represented as a 2D integer array edges,
where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi.

Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex start to vertex end.

Given edges and the integers n, start, and end, return true if there is a valid path from start to end, or false otherwise.

TODO
    OPTIMIZATION
    REVIEW
"""

from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        def _build_adjacency_list(length, edge_list):
            adjacency_list = {i: [] for i in range(length)}
            for edge in edge_list:
                adjacency_list[edge[0]].append(edge[1])
                adjacency_list[edge[1]].append(edge[0])

            return adjacency_list

        def _dfs(at):
            if at == end:
                return True
            if not is_visited[at]:
                is_visited[at] = True
                neighbours = graph[at]
                for node in neighbours:
                    if _dfs(node):
                        return True
            return False

        graph = _build_adjacency_list(n, edges)
        is_visited = [False] * n
        result = _dfs(start)
        return result


S = Solution()
print(S.validPath(10,[[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]], 7, 5))
