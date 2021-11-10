"""
Kahn's Algorithm
TODO:
- Memory optimization
- the secret of the index mechanism
"""

from typing import List, Dict
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def _build_adjacency_list(length: int, edge_list: List[List[int]]) -> Dict:
            _adjacency_list = {i: [] for i in range(length)}
            for edge in edge_list:
                _adjacency_list[edge[1]].append(edge[0])
            return _adjacency_list

        adjacency_list = _build_adjacency_list(numCourses, prerequisites)

        # build in-degree array
        in_degrees = [0] * numCourses
        for i in range(numCourses):
            for child in adjacency_list[i]:
                in_degrees[child] += 1

        # build the queue that contains all in-degree nodes (nodes with no incoming edges)
        queue = deque(maxlen=numCourses)
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)

        index = 0
        order = [0] * numCourses
        while queue:
            node = queue.popleft()
            order[index] = node
            for child in adjacency_list[node]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    queue.append(child)
            index += 1

        if index != numCourses:
            return False
        return True


S = Solution()
print(S.canFinish(numCourses=2, prerequisites=[[1, 0]]))
