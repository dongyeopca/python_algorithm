s = input()
reverse_s = s[::-1]
count =0
for i in range(len(s)):
    if s[i]==reverse_s[i]:
        count+=1
if count == len(s):
    print(1)
else:
    print(0)
