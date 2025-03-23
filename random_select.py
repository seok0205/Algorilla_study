import random

people = ['임연지', '유정석', '윤혜진', '김지수', '김동규', '김가현']
problems = ['2930. 힙', '1210. Ladder2', '13038. 교환학생']

random.shuffle(people)
random.shuffle(problems)

selected_people = people[:5]
selected_problems = problems[:5]
zipped_list = list(zip(selected_people, selected_problems))
for entry in zipped_list:
    print(f"발표자: {entry[0]} - 문제: {entry[1]}")
