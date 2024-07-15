graph= {1:[2,4,3],2:[5],3:[4,5],4:[],5:[]}
visited = set()
def dfs(visited,graph,root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited,graph,neighbour)
        


dfs(visited,graph,1)    