n,k = map(int,input().split())
person = [i for i in range(1,n+1)]
count = 0#인덱스번호
answer = []

for i in range(n):
    count +=k-1
    if count>=len(person):
        count = count%len(person)
    
    answer.append(str(person.pop(count)))
print("<",", ".join(answer)[:],">",sep="")