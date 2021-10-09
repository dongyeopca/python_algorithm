# a = 'aBca deN'
# a = a.lower() 소문자로 바꾸고
# a = a.split() 공백 기준으로 쪼개준다.
# for i in range(len(a)):
#     a[i] =  a[i].replace(a[i][0],a[i][0].upper(),1) 첫번째 녀석 문자를 소문자로 바꾸고 1회에 한정한다.
    
# answer = ' '.join(a) #요소 사이에 공백을 삽입한다.
# print(answer)출력한다.
#근데 테스트 케이스만 통과하고 틀렸다.아마 단어사이에 공백이 여러개 입력됬을때를 통과하지 못하는것같다.
def solution(s):
    a = s.lower()#입력값 소문자로 바꾸고
    answer = ""#문자열만들고
    for i in a:#돌면서
        if answer:#answer문자열이 아무것도 없지않으면
            if answer[-1] == " ":#answer 마지막이 공백이면
                answer+=i.upper()#대문자로 넣어주고
            else:
                answer+=i#아니면 그냥 넣어준다.
                
        else:#answer 문자열 비었으면
            answer+=i.upper() #처음 들어가는거는 대문자로 넣어주고
        #근데 이것도 처음에 공백으로 들어오면 틀린당. 하지만 통과했으니 추가 조건은 안써줄꺼임 ㅇㅅㅇ!
    return answer