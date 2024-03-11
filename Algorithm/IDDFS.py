def iddfs(graph,start,target,max_depth):
    for depth in range(max_depth+1):
        visited=set()
        if dls(graph,start,target,depth,visited):
            return True
        return False

def dls(graph,node,target,depth,visited):
    if depth==0 and node==target:
        return True

    if depth>0:
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dls(graph,node,target,depth,visited):
                    return True
                return False

graph={
    'A':['B','C'],
    'B': ['D', 'E'],
    'C': ['F', 'A'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

start_node='A'
target_node='C'
maximum_depth=3

if iddfs(graph,start_node,target_node,maximum_depth):
    print('Target node',target_node,'found with maximum depth of',maximum_depth)
else:
    print('Target node', target_node, 'found with maximum depth of', maximum_depth)