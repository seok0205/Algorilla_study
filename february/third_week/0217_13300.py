# 남남 여여
# 같은 학년 같은 반
# 한 방에 한 명 배정도 가능
# 필요한 방의 최소 개수

num_of_students, max_num_per_room = map(int, input().split())
students_arr = [list(map(int, input().split())) for _ in range(num_of_students)] # gender, grade
counts_female = [0] * 7
counts_male = [0] * 7
for gender, grade in students_arr:
    if gender == 0: # female
        counts_female[grade] += 1
    else:
        counts_male[grade] += 1

counts = 0
for count in counts_female:
    if 1 <= count <= max_num_per_room:
        counts += 1
    elif count > max_num_per_room:
        counts += (count // max_num_per_room)
        if count % max_num_per_room:
            counts += 1
for count in counts_male:
    if 1 <= count <= max_num_per_room:
        counts += 1
    elif count > max_num_per_room:
        counts += (count // max_num_per_room)
        if count % max_num_per_room:
            counts += 1

print(counts)