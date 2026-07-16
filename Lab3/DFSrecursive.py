#DFS Algorithm (Recursive)
graph = {
    'A': ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []

}
visited = []

def dfs(visited, graph, node):
    if node not in visited:
        visited.append(node)
        print(node, end = ' ')
    for neighbour in graph[node]:
        dfs(visited, graph, neighbour)

print('=' * 50)
print("DEPTH-FIRST SEARCH TRAVERSAL (ITERATIVE)")
print("=" * 50)
print("DFS Order: ", end='')
dfs(visited, graph, 'A')
print()
print("=" * 50)
print("Program by: Qureen Bhandari")
print("Roll No: 24")
