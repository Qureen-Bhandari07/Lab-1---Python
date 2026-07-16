#DFS Algorithm (Recursive)
graph = {
    'A': ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : [],
    'F' : []

}
visited = [] #list for visited nodes

def dfs_recursive(visited, graph, node):
    if node not in visited:
        visited.append(node)
        print(node, end = ' ')
    for neighbour in graph[node]:
        dfs_recursive(visited, graph, neighbour)

print('=' * 50)
print("DEPTH-FIRST SEARCH TRAVERSAL (Recursive)")
print("=" * 50)
print("DFS Order: ", end='')
dfs_recursive(visited, graph, 'A')
print()
print("=" * 50)
print("Program by: Qureen Bhandari")
print("Roll No: 24")
