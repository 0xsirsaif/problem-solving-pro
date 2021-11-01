"""

"""

from typing import List, Dict
from collections import deque, defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency_list = defaultdict(set)

        for i, j in prerequisites:
            adjacency_list[j].add(i)

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

        # check for cyclic path
        if index != numCourses:
            return []
        return order


S = Solution()
print(S.findOrder(numCourses=2, prerequisites=[[1, 0]]))
