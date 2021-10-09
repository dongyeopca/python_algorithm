#dfs + bfs
 

n,m,v = map(int,input().split())
matrix = [[0]*(n+1) for i in range(n+1)]
for i in range(m):
    a,b = map(int,input())
    matrix[a][b] = matrix[b][a] = 1

def dfs(x,y):

