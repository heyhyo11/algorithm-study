# 풀이 참고

n, m = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 1
cnt = 0
while right <= n and left <= right:

    sum_nums = nums[left:right]
    total = sum(sum_nums)
    # 합이 m이면 cnt+1, 오른쪽으로 한 칸 이동
    if total == m:
        cnt += 1
        right += 1
    # 합이 m 이하면 오른쪽으로 한 칸 이동
    elif total < m:
        right += 1
    # 합이 m 초과면 왼쪽 포인터를 오른쪽으로 한 칸 이동
    else:
        left += 1
print(cnt)