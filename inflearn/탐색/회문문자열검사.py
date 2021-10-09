n = int(input())
for i in range(n):
    word = input()
    word.upper()
    rev = word[::-1]
    if word == rev:
        print("#%d YES"%int(i+1))
    else:
        print("#%d NO"%int(i+1))

