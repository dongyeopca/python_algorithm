def solution(n, arr1, arr2):
    puzzle = [""]*n #리스트안에 문자열을 지도의 길이만큼 곱해준다.
    for i in range(len(arr1)):
        arr1[i] = format(arr1[i],'b').rjust(n,'0')#10진수로 표현된 각 행을 이진수로 변환해주고 n의 길이보다 짧은 녀석은 앞에 0을 채워준다.
        arr2[i] = format(arr2[i],'b').rjust(n,'0')#마찬가지이다.
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':#arr1과 arr2중 하나라도 1이 있으면
                puzzle[i] += '#'#퍼즐에 '#'을 더해주고
            else:
                puzzle[i]+= ' '#그게 아니면 공백을 더해준다.
    return puzzle #결과값 리턴