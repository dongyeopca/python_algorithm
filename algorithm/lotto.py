# def solution(lottos, win_nums):
#     counter = 0
#     count0 = 0
#     for i in lottos:
#         if i == 0:
#             count0 += 1
#         else:   
#             for j in win_nums:
#                 if i ==j:
#                     counter += 1 
#     best = count0+counter
#     worst = counter
#     if best != 0:
#         bestrank = 7-best
#     else:
#         bestrank = 6

#     if worst != 0:
#         worstrank = 7-worst
#     else:
#         worstrank = 6

#     answer = [bestrank,worstrank]
#     return answer

from collections import deque
def solution(maps):
    h = len(maps)
    l = len(maps[0])
    queue = deque()
    queue.append((0,0))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while queue:
        x,y= queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=l or ny<0 or ny>=h:
                continue
            if maps[ny][nx] == 0:
                continue
            if maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x]+1
                queue.append((nx,ny))
                
    print(maps[l-1][h-1])
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])