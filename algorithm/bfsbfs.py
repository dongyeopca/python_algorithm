
n,m,v= map(int,input().split())
matrix = [[0]*(n+1) for i in range(n+1)]
visited=[]
for i in range(m):
    a,b = map(int,input().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(start,visited):
    visited+=[start]
    for i in range(1,n+1):
       if matrix[start][i] == 1 and (i not in visited):
           dfs(i,visited)
    return visited

dfs(v,visited)

# from collections import deque
# def bfs(start):
#     visitied = [start]
#     queue = deque([start])
#     while queue:
#         n=queue.popleft()
#         for i in range(len(matrix[n])):
#             if matrix[n][i] == 1 and (i not in visitied):
#                 visitied.append(i)
#                 queue.append(i)
#     return visitied

print([0]*10)