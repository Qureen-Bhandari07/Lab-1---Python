#BFS Algorithm
graph = {
    'A': ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : ['G','H'],
    'E' : ['I'],
    'F' : [],
    'G' : [],
    'H' : [],
    'I' : []

}
visited=[] #List for visited nodes
queue = [] #Initialize a stack

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        m=queue.pop(0)
        print(m, end = ' ')

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                print('Visited nodes:',node)
                print('Queue : ',queue)
    return visited, queue
print("=" * 50)
print("BREADTH-FIRST SEARCH TRAVERSAL")
print("=" * 50)
print("BFS Order: ", end='')

visited, queue = bfs(visited, graph, 'A')
print()  # Adds a new line right after the BFS traversal characters print out
print()  # Adds an extra blank line for visual spacing

print("Visited Nodes: ", visited)
print("Queue: ", queue)
print("=" * 50)
print("Program by: Qureen Bhandari")
print("Roll No: 24")