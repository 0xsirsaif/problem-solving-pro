"""
problem
    You have recently started playing a brand new computer game called "Mr. President".
    The game is about ruling a country, building infrastructures and developing it.

    Your country consists of N cities and M bidirectional roads connecting them.
    Each road has assigned a cost of its maintenance. The greatest achievement in the game is called "Great administrator"
    and it is given to a player who manage to have all cities in the country connected by roads in such a way that
    it is possible to travel between any two cities and that the sum of maintenance costs of these roads is not greater than K.

    This is very hard to accomplish, but you are very close to do it.
    More precisely, you have just discovered a new method of transforming standard roads into super roads,
    with cost of maintenance just 1, due to their extreme durability.

    The bad news is that it is very expensive to transform a standard road into a super road,
    but you are so excited that you are going to do it anyway.

    In addition, because you have a lot of other expenses, you also want to first demolish as many roads as possible in order
    to safe some money on their maintenance first and then start working on getting the achievement.
    You can demolish any road in the country and that operation does not cost you anything.

    Because you want to spend the absolutely minimum money in order to get the achievement,
    you are interested in the smallest number of transformations of standard roads into super roads in such a way that you can do that.

Input format:
    In the first line there are 3 integers N, M and K denoting the number of cities in the country,
    the number of roads in it and the desired sum of costs of maintenance.
    M lines describing these roads follow. In each of them there are 3 integers A, B and C, where A and B
    denote the endpoints of the road while C denotes the cost of its maintenance.

Output:
    In a single line, output the minimum number of roads which need to be transformed in order to get the achievement.
    If you cannot do it no matter what, output -1.

Constraints:
    2 <= N, M <= 106
    0 <= K <= 1018
    1 <= A, B <= N and A != B
    1 <= C <= 106

TODO
    Wrong Answers?
    REVIEW
"""


def take_inputs():
    n, m, k = [int(i) for i in input().split()]
    edge_list = [tuple([int(i) for i in input().split()]) for _ in range(m)]

    return kruskal(n, edge_list, k)


def kruskal(num_nodes, edges_list, cost):
    def _sort_edges(edges):
        return sorted(edges, key=lambda _edge: _edge[2])

    def _construct_union_find(n):
        parent = [0] * (n + 1)
        for i in range(1, n+1):
            parent[i] = i
        return parent

    def _find(node):
        root = node
        while root != parent_list[node]:
            root = parent_list[node]

        # path compression
        while node != root:
            next_node = parent_list[node]
            parent_list[node] = root
            node = next_node

        return root

    def _unify(start, end):
        root1, root2 = _find(start), _find(end)
        if root1 == root2:
            return
        parent_list[root1] = root2

    parent_list = _construct_union_find(num_nodes)

    sorted_edges = _sort_edges(edges_list)
    print(">>>", sorted_edges)
    working_cost = 0
    roads = []
    for edge in sorted_edges:
        node1, node2, weight = edge
        working_cost += weight
        if _find(node1) != _find(node2) and working_cost <= cost:
            _unify(node1, node2)
            roads.append(edge)

    return len(roads)


print(take_inputs())
