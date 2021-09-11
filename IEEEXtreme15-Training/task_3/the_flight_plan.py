"""
Hacker earth

Problem
    You are given flights route map of a country consisting of N cities and M undirected flight routes.
    Each city has an airport and each airport can work as layover.
    The airport will be in two states, Loading and Running. In loading state, luggage is loaded into the planes.
    In the running state, planes will leave the airport for the next city.
    All the airports will switch their states from Loading to Running and vice versa after every T minutes.
    You can cross a city if its airport state is running. Initially, all the airports are in running state.
    At an airport, if its state is loading, you have to wait for it to switch its state to running.
    The time taken to travel through any flight route is C minutes.

Find the lexicographically smallest path which will take the minimum amount of time (in minutes) required to move from city X to city Y.

It is guaranteed that the given flight route map will be connected. Graph won't contain multiple edges and self loops.

TODO
    COMPLETE: lexicographically!
    REVIEW
"""


def take_inputs():
    def _build_adjacency_list(edges):
        nodes = list(set([item for sublist in edges for item in sublist]))
        adjacency_list = {i: [] for i in nodes}
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])

        return adjacency_list

    n, m, t, c = [int(i) for i in input().split()]
    edge_list = [[int(i) for i in input().split()] for _ in range(m)]
    start, end = [int(i) for i in input().split()]

    adjacency_list = _build_adjacency_list(edge_list)

    return bfs(start, end, adjacency_list)


def bfs(start, end, adjacency_list):
    prev = solve(start, adjacency_list)

    return reconstruct_path(start, end, prev)


def solve(start, adjacency_list):
    q = [start]

    is_visited = {k: False for k in adjacency_list.keys()}
    is_visited[start] = True
    prev = {k: False for k in adjacency_list.keys()}
    while q:
        node = q.pop()
        neighbours = adjacency_list.get(node) or []
        for next_node in neighbours:
            if not is_visited[next_node]:
                q.insert(0, next_node)
                is_visited[next_node] = True
                prev[next_node] = node
    return prev


def reconstruct_path(s, e, prev):
    path = [e]
    _next = prev.get(e)
    while _next:
        path.append(_next)
        _next = prev.get(_next)

    return path[::-1]


print(take_inputs())