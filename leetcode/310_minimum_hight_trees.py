"""

"""

from typing import List
import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def _dfs(root, graph, visited, h, max_h):
            print(root, h)
            visited.add(root)
            if not (graph[root] - visited):
                return h
            for child in graph[root] - visited:
                _dfs(child, graph, visited, h+1, max_h)
            return 1

        adjacency_list = collections.defaultdict(set)
        for u, v in edges:
            adjacency_list[u].add(v)
            adjacency_list[v].add(u)

        for node in range(n):
            print(">>>>")
            visited_ = set()
            _dfs(node, adjacency_list, visited_, 0, 0)
            break

        return []


S = Solution()
print(S.findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]))
