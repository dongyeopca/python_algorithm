#나이트는 수평으로 두칸이동 수직한칸이동 or 수직으로 두칸이동 수평 한칸이동
place = input()
row = int(place[1])
column = int(ord(place[0]))-int(ord('a'))+1
result = 0
steps = [
    (-2,-1),(-2,1),(2,-1),(2,1),(-1,2),(1,2),(-1,-2),(1,-2)
]

for step in steps:
    next_row = row+ step[0]
    next_column = column+step[1]
    if next_row>=1 and next_row<=8 and next_column>=1 and next_column<=8:
        result +=1

print(result)