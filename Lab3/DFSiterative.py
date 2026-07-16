#DFS Algorithm (Iterative using Stack)
graph = {
    'A': ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []

}
visited = []
stack = []

def dfs(visited, graph, node):
    stack.append(node)
    visited.append(node)

    while stack:
        m = stack.pop()
        print(m, end = ' ')

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)
print("=" * 50)
print("DEPTH-FIRST SEARCH TRAVERSAL (ITERATIVE)")
print("=" * 50)
print("DFS Order: ", end='')
dfs(visited, graph, 'A')
print()
print("=" * 50)
print("Program by: Qureen Bhandari")
print("Roll No: 24")

