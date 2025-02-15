import random

'''
조창현 결석
1979. 어디에 단어가 들어갈 수 있을까는 저번 주 문제에 있으므로 제외
'''

people = ['임연지', '유정석', '윤혜진', '김지수', '김동규', '김가현']
problems = ['22375. 스위치 조작', '20397. 돌 뒤집기 게임 2', '18575. 풍선팡 보너스 게임', '3499. 퍼펙트 셔플', '1959. 두 개의 숫자열']

random.shuffle(people)
random.shuffle(problems)

selected_people = people[:5]
selected_problems = problems[:5]
zipped_list = list(zip(selected_people, selected_problems))
for entry in zipped_list:
    print(f"발표자: {entry[0]} - 문제: {entry[1]}")
