matrix = [[0,0,0],[0,0,0],[0,0,0]]
road = [[1,2,1],[1,2,2]]
for i in range(1,len(matrix)):
    if matrix[road[i][0]][road[i][1]]<=road[2]:
        matrix[road[i][0]][road[i][1]] = matrix[road[i][1]][road[i][0]] = road[i][2]
print(matrix)