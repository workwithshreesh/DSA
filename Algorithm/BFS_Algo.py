from collections import deque
def bfs(graph,start):
    visited=set()
    queue=deque([start])
    visited.add(start)
    while queue:
        node=queue.popleft()
        print(node,end='')

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph={
    'A':['B','C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node='A'
print('BFS traversal starting from node',start_node)
bfs(graph,start_node)