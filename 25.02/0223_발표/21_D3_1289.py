'''
D3 1289 원재의 메모리 복구하기

비트중 한자리 골라 0, 1인지 결정하면 메모리 끝까지 덮어씌움
예로 0100에서 3번째 비트 골라 1로 설정하면 0111이 됨
원래 상태가 주어질때 초기화 상태에서 원래 상태로 돌아가는데 최소 몇번을 고쳐야하는 지 계산
'''

T = int(input())

for tc in range(1, T+1):
    target = list(map(int, input()))
    bit = [0] * len(target)
    result = 0
    
    for i in range(len(bit)):       # 비트 길이(탐색해야할 리스트) 만큼 반복
        if bit[i] != target[i]:     # 초기화된 상태의 자리와 목표 리스트의 자리가 다르면
            result += 1             # 바꾼 횟수 증가
            num = bit[i] ^ 1        # 0 or 1 변환
            for j in range(i, len(bit)):        # 뒷자리 모두
                bit[j] = num                    # 같은 숫자로 설정
    
    print(f'#{tc} {result}')