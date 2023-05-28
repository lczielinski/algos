import sys


def run_bellman_ford(graph, vertices, start):
    prev_lengths = dict()
    prev_lengths[start] = 0
    for t in vertices:
        prev_lengths[t] = sys.maxsize
        for ((u, v), l) in graph.items():
            if u == start and v == t:
                prev_lengths[t] = l
                break
    print(prev_lengths)

    for _ in range(len(vertices) + 1):
        lengths = dict()
        lengths[start] = 0
        for t in vertices:
            lengths[t] = prev_lengths[t]
            for ((u, v), l) in graph.items():
                if v == t:
                    lengths[t] = min(lengths[t], l + prev_lengths[u])
        print(lengths)
        prev_lengths = lengths


graph = dict()
graph[("a", "b")] = -12
graph[("b", "d")] = 4
graph[("b", "t")] = 3
graph[("c", "a")] = 6
graph[("c", "b")] = -4
graph[("d", "t")] = -1
graph[("d", "c")] = 1
graph[("d", "f")] = -3
graph[("e", "d")] = 1
graph[("e", "t")] = -2
graph[("s", "c")] = 8
graph[("s", "d")] = 7
graph[("s", "f")] = 5
graph[("f", "e")] = 3
graph[("f", "g")] = -2
graph[("g", "e")] = 8
vertices = set(["a", "b", "c", "d", "e", "f", "g", "t"])
run_bellman_ford(graph, vertices, "s")
