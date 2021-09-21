"""
HackerEarth :
https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/practice-problems/algorithm/lonelyisland-49054110/

TODO:
    REVIEW & NOTES
    COMPLETE
"""


def take_inputs():
    def _build_adjacency_list(length, edges):
        adjacency_list = {i: [] for i in range(length + 1)}
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])

        return adjacency_list

    n, m, k = [int(i) for i in input().split()]
    edge_list = [tuple([int(i) for i in input().split()]) for _ in range(m)]

    print(edge_list)
    graph = _build_adjacency_list(n, edge_list)
    print(graph)
    return khan_algorithm(n, graph)


def khan_algorithm(num_nodes, graph):
    in_degree = [0] * (num_nodes + 1)

    for key, values in graph.items():
        for i in values:
            in_degree[i] += 1

    print(in_degree)
    queue = []
    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            queue.append(i)

    ordering = []
    next_idx = 0
    while queue:
        vertex = queue.pop(0)
        next_idx += 1
        ordering.append(vertex)
        for x in graph[vertex]:
            in_degree[x] -= 1
            if in_degree[x] == 0:
                queue.append(x)

    if next_idx != len(graph):
        return -1
    return ordering[-1]


print(take_inputs())