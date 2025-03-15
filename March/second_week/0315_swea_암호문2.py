'''
5
10 11 12 13 14
3
I 1 3 100 101 102 I 4 2 400 401 D 2 4

19
701633 517247 207227 598906 709204 177422 933135 361253 641488 272037 700207 210546 897237 133041 350385 701520 298460 312226 606874
2
D 10 3 I 6 6 291139 808642 764059 913376 124313 256337
'''

def sort_passcode(curr_passcode, start_idx, nums):
    new_passcode = []
    i = 0
    while i < start_idx:
        new_passcode.append(curr_passcode[i])
        i += 1

    new_passcode.extend(nums)

    if i < len(curr_passcode):
        new_passcode.extend(curr_passcode[i:])

    return new_passcode


for t in range(1, 11):
    len_passcode = int(input())
    passcode = list(input().split())
    num_commands = int(input())
    commands = list(input().split())
    count = 0
    while count < num_commands:
        for i in range(len(commands)):
            if commands[i] == 'I':
                len_nums = int(commands[i + 2])
                idx, nums = int(commands[i + 1]), commands[i + 3:i + 3 + len_nums]
                passcode = sort_passcode(passcode, idx, nums)
                count += 1
            elif commands[i] == 'D':
                idx, len_nums = int(commands[i + 1]), int(commands[i + 2])
                for _ in range(len_nums):
                    passcode.pop(idx)
                count += 1

    print(f"#{t}", *passcode[:10])
