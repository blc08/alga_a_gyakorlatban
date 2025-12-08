import sys
from collections import deque


def isBipartite(start_node, graph, colors):
    queue = deque([start_node])
    colors[start_node] = 1

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if colors[v] == 0:
                colors[v] = -colors[u]
                queue.append(v)
            elif colors[v] == colors[u]:
                return False
    return True


def solve(scenario_idx, num_bugs, graph):
    colors = [0] * (num_bugs + 1)  # 0: Unvisited, 1: A, -1: B
    suspicious = False

    for i in range(1, num_bugs + 1):
        if colors[i] == 0:
            if not isBipartite(i, graph, colors):
                suspicious = True
                break

    print(f"Scenario #{scenario_idx}:")
    if suspicious:
        print("Suspicious bugs found!")
    else:
        print("No suspicious bugs found!")


if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    iterator = iter(input_data)

    try:
        t = int(next(iterator))
    except StopIteration:
        t = 0

    for i in range(1, t + 1):
        try:
            n = int(next(iterator))  # Number of bugs
            m = int(next(iterator))  # Number of interactions

            g = [[] for _ in range(n + 1)]

            for _ in range(m):
                u = int(next(iterator))
                v = int(next(iterator))
                g[u].append(v)
                g[v].append(u)

            solve(i, n, g)

        except StopIteration:
            break