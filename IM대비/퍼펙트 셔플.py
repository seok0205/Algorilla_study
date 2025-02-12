T = int(input())
for t in range(1, T+1):
    # 카드의 수
    N = int(input())
    arr = list(input().split())
    # 카드가 홀수개이면 첫번째 더미에 1개를 더 넣어준다.
    arr1 = arr[:(N//2)+(N%2)] 
    arr2 = arr[(N//2)+(N%2):]
    result = []
    for i in range(N//2+N%2):
        result.append(arr1[i])
        # i 가 arr2의 범위를 벗어나면 for문 종료
        if i == len(arr2):   
            break                    
        else:
            result.append(arr2[i])
    
    # # while문 사용해서 풀기
    # i = 0 
    # while i < len(arr1):  # arr1의 길이만큼 반복
    #     result.append(arr1[i])  # 첫 번째 더미에서 추가
    #     if i < len(arr2):  # 두 번째 더미에서 추가 (범위 초과 방지)
    #         result.append(arr2[i])
    #     i += 1  # 인덱스 증가
    print(f'#{t}', ' '.join(result))
