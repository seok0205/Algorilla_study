import random

people = ['임연지', '유정석', '윤혜진', '김지수', '김동규', '김가현']
problems = ['1197. 최소 스패닝 트리', '2606. 바이러스', '2644. 촌수계산', '2667. 단지 번호 붙이기', '11724. 연결 요소의 개수']

random.shuffle(people)
random.shuffle(problems)

selected_people = people[:5]
selected_problems = problems[:5]
zipped_list = list(zip(selected_people, selected_problems))
for entry in zipped_list:
    print(f"발표자: {entry[0]} - 문제: {entry[1]}")
