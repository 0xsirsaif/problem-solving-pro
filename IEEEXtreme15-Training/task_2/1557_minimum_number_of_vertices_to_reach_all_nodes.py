"""
Optimizations?
    - instead of a function to build adjacency list, use comprehension?
    - dfs copy a lot of data [visited_nodes, graph, result]
        - make use of the outer variables? -> disadvantage: function side effect

"""

from typing import List, Dict


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        def _build_adjacency_list(length: int, edge_list: List[List[int]]) -> Dict:
            _adjacency_list = {i: [] for i in range(length)}
            for edge in edge_list:
                _adjacency_list[edge[0]].append(edge[1])

            return _adjacency_list

        def _dfs(node: int, visited_nodes: List, graph: Dict, result: List):
            for j in graph[node]:
                if visited_nodes[j] is False:
                    _dfs(j, visited_nodes, graph, result)
                    visited_nodes[j] = True
                if result[j] is True:
                    result[j] = False
            return visited_nodes

        adjacency_list = _build_adjacency_list(n, edges)

        visited = [False] * n
        in_degree_nodes = [False] * n
        for i in range(n):
            if visited[i] is False:
                in_degree_nodes[i] = True
                _dfs(i, visited, adjacency_list, in_degree_nodes)

        return [i for i, j in enumerate(in_degree_nodes) if j]


S = Solution()
print(S.findSmallestSetOfVertices(n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]))