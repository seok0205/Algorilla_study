'''
문자를 입력하고 나서 입력된 문자가 연속해서 나타나는 경우만이 그룹단어.
똑같은 문자가 연속적이지 않고 비연속적으로 후에 한번 더 입력된다면 그것은 그룹단어가 아니다.

example:
aaabba는 a가 서로 떨어진 상태로 나타나 그룹 단어가 아님
yyuujjkk는 모두 연속해서 나와서 그룹 단어
yuj도 각자 연속해서 나타나 그룹 단어

제한 사항:
N <= 100
단어는 알파벳 소문자, 중복 X, 길이 최대 100
'''

num = int(input())  # 첫째 줄에 입력받을 단어의 개수 N 입력
groupWord = num # 최대 그룹단어 개수

for i in range(num):    # 반복해서 단어를 입력 받고
    word = input()

    for j in range(0, len(word)-1): # 문자열을 순회하면서
        if word[j] == word[j+1]:    # 연속해서 오는 문자가 같다면 패스
            pass
        elif word[j] in word[j+1:]: # 연속해서 오지 않으면 그룹 단어의 개수 1 감소
            groupWord -= 1
            break   # 그룹단어가 아니면 더이상 순회할 의미가 없으므로 반복문 탈출

print(groupWord)