import random

people = ['임연지', '유정석', '윤혜진', '김지수', '김동규', '김가현']
problems = ['21425. +=', '11315. 오목 판정', '5789. 현주의 상자 바꾸기', '4615. 재미있는 오셀로 게임', '2805. 농작물 수확하기', '1873. 상호의 배틀필드', '1289. 원재의 메모리 복구하기']

random.shuffle(people)
random.shuffle(problems)

selected_people = people[:5]
selected_problems = problems[:5]
zipped_list = list(zip(selected_people, selected_problems))
for entry in zipped_list:
    print(f"발표자: {entry[0]} - 문제: {entry[1]}")
