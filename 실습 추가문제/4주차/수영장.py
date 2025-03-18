def min_cost_swimming(pool_usage, costs):
    dp = [0] * 13  # 1월~12월까지 최소 비용을 저장하는 DP 배열

    for i in range(1, 13):  # 1월부터 12월까지 계산
        daily_cost = dp[i-1] + pool_usage[i] * costs[0]  # 1일 이용권 사용
        monthly_cost = dp[i-1] + costs[1]  # 1달 이용권 사용
        three_month_cost = dp[max(0, i-3)] + costs[2]  # 3달 이용권 사용
        yearly_cost = dp[max(0, i-12)] + costs[3]  # 1년 이용권 사용

        dp[i] = min(daily_cost, monthly_cost, three_month_cost, yearly_cost)

    return dp[12]  # 12월까지 최소 비용 반환

# 수영장 최소비용으로 다니기
T = int(input())
for t in range(1, T+1):
    # 각 이용권들의 가격
    # 1일, 1달, 3달, 1년
    cost = list(map(int, input().split()))
    # 1년 이용 계획
    arr = list(map(int, input().split()))
    arr1 = [0]
    arr1.extend(arr)
    result = min_cost_swimming(arr1, cost)
    print(f'#{t} {result}')