graph = {
    'A': {'B', 'C', 'D', 'E'},
    'B': {'A', 'F', 'G'},
    'C': {'A', 'K'},
    'D': {'A', 'M'},
    'E': {'A', 'L'},
    'F': {'B', 'H'},
    'G': {'B', 'I'},
    'H': {'F', 'J'},
    'I': {'G', 'J'},
    'J': {'H', 'I', 'Z'},
    'K': {'C', 'N', 'O'},
    'L': {'E', 'R'},
    'M': {'D', 'O'},
    'N': {'K', 'P'},
    'O': {'K', 'M', 'Q'},
    'P': {'N', 'Z'},
    'Q': {'O', 'Z'},
    'R': {'L', 'S', 'T'},
    'S': {'R'},
    'T': {'R'},
    'Z': {'J', 'P', 'Q'}
}


def dfs(graph, start):
    visited, stack = set(), [start]
    result = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            stack.extend(graph[vertex] - visited)
    return result


def bfs(graph, start):
    visited, queue = set(), [start]
    result = []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            queue.extend(graph[vertex] - visited)
    return result


dfs_result = dfs(graph, 'A')
bfs_result = bfs(graph, 'A')

# Output the results of DFS and BFS
print("DFS Result:", dfs_result)
print("BFS Result:", bfs_result)

