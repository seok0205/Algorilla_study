
# bin, int 함수 쓴 경우
# T = int(input())
# for t in range(1, T+1):
#     one_len, zero_len = map(int, input().split())
#     max_binary = '1'*one_len + '0'*zero_len
#     min_binary = '1' + '0'*zero_len + '1'*(one_len-1)
#     answer = int(max_binary, 2) * int(min_binary, 2)
#     answer_to_binary = bin(answer)
#     print(f"#{t} {answer_to_binary.count('1')}")

# 함수 안 쓴 경우 - 시간초과로 fail
def binary_to_decimal(string):
    binary = string[::-1]
    decimal = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            decimal += 2**i
    return decimal

def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        if decimal & 0x1:
            binary += '1'
        else:
            binary += '0'
        decimal >>= 1
    return binary

T = int(input())
for t in range(1, T+1):
    one_len, zero_len = map(int, input().split())
    max_binary = '1'*one_len + '0'*zero_len
    min_binary = '1' + '0'*zero_len + '1'*(one_len-1)
    multiplied = binary_to_decimal(max_binary) * binary_to_decimal(min_binary)
    result = decimal_to_binary(multiplied)

    print(f"#{t} {result.count('1')}")