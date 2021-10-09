#두개의 길이가 더 긴거에 더 큰값
#두번째로 길이 긴 녀석과 같아질때까지 제일 긴애한테 9 8 순으로 넣어줌
#같아지면 그 부분에 녀석이 더 많이 나타나는 애한테 큰 수를 넣어주고 그다음 큰수를 같은 녀석한테 넣어줌
n = int(input())
alphabet = []
length=[]
for _ in range(n):
    alphabet.append(input())

alphabet.sort(reverse=True)#길이가 긴거 순으로 정렬
for i in alphabet:
    length.append(len(i))
for i 
어려웅러눔이룸ㄴㅇ.ㄹ