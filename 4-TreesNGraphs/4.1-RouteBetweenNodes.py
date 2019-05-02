from collections import deque, defaultdict


# graph = {
#     1: [2, 3],
#     2: [4, 5, 6]
# }

graph = defaultdict(list)
graph[1] = [2, 3]
graph[2] = [4, 5, 6]

def is_route_present(graph, u, v):
    if graph is None:
        return

    visited_nodes = set()

    q = deque()
    q.append(u)
    visited_nodes.add(u)

    while len(q) > 0:
        current = q.popleft()

        for neighbour in graph[current]:
            if neighbour not in visited_nodes:
                q.append(neighbour)
                visited_nodes.add(neighbour)

                if neighbour == v:
                    return True

    return False


""" Driver code """

print(is_route_present(graph, 1, 6))
print(is_route_present(graph, 1, 2))
print(is_route_present(graph, 2, 3))


