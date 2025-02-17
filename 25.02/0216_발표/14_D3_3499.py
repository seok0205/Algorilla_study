'''
D3 3499 퍼펙트 셔플

카드 덱을 정확히 절반으로 나누고 나눈 것들에서 교대로 카드를 뽑아 새 덱을 만드는 것이 퍼펙트 셔플
N개의 카드가 있는 덱이 주어지면 퍼펙트 셔플 시 어떤 순서가 출력되는지 구하는 문제
N이 만약 홀수면, 교대로 놓을 때 먼저 놓는 쪽에 한 장이 더 들어감

입력:
테스트 케이스 수 T
자연수 N (1이상 1000이하)
N개의 카드 이름 공백 구분 입력(카드 이름은 알파벳 대문자 및 '-'만으로 이루어짐. 길이 80이하)
'''


def shuffle(a, b):          # 셔플 함수
    shuffled_lst = []           # 셔플된 결과 담을 리스트
    for i in range(len(b)):         # b의 길이는 a보다 하나 짧거나 같으므로 b를 기준
        shuffled_lst.append(a[i])
        shuffled_lst.append(b[i])
    else:                           # for문을 다 돌리면 N이 홀수일 때 a의 끝 원소가 하나 남음
        if len(a) > len(b):         # 이 경우엔 a가 더 길 때 이므로
            shuffled_lst.append(a[-1])  # a의 남은 끝 원소만 추가
            
    return shuffled_lst


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(str, input().split()))
    
    if N % 2:       # N이 홀수면 한 장 더 포함되게 분할
        first_half, second_half = cards[:N//2+1], cards[N//2+1:]
    else:
        first_half, second_half = cards[:N//2], cards[N//2:]
        
    result = shuffle(first_half, second_half)   # shuffle() 함수로 퍼펙트 셔플된 리스트 반환
    
    print(f"#{tc} {' '.join(result)}")