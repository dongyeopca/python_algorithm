# from collections import deque
# def solution(N, road, K):
#     matrix = [[0]*(N+1) for i in range(N+1)]
#     for i in range(len(road)):
#         if matrix[road[i][0]][road[i][1]] != 0 and matrix[road[i][0]][road[i][1]]<=road[i][2]:
#             continue
#         else:
#             matrix[road[i][0]][road[i][1]] = matrix[road[i][1]][road[i][0]] = road[i][2]
#     queue = deque([1])
#     visited = [1]
#     answer = 0
#     while queue:
#         n=queue.popleft()
#         for i in range(1,N+1):
#             if matrix[n][i] !=0 and matrix[n][i]<=K and (i not in visited):
#                 queue.append(i)
#                 visited.append(i)
#                 answer+=1
#                 for j in range(1,len(matrix[i])):
#                     if matrix[i][j] != 0 and (j not in visited):
#                         matrix[i][j]+=matrix[n][i]
#     print(matrix)
#     return answer+1

a = [1,2,3,4]
print(a.index(max(a)))