import random

people = ['임연지', '유정석', '윤혜진', '김지수', '김동규', '김가현', '조창현']
problems = ['11092. 최대 최소의 간격', '9386. 연속한 1의 개수', '6485. 삼성시의 버스 노선', '1979. 어디에 단어가 들어갈 수 있을까', '1974. 스도쿠 검증']

random.shuffle(people)
random.shuffle(problems)

selected_people = people[:5]
selected_problems = problems[:5]
zipped_list = list(zip(selected_people, selected_problems))
for entry in zipped_list:
    print(f"발표자: {entry[0]} - 문제: {entry[1]}")
