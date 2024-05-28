def solution(brown, yellow):
    brown = (brown - 4) // 2
    yellow_list = [i for i in range(1, brown) if i * (brown - i) == yellow]
    return [max(yellow_list) + 2, min(yellow_list) + 2]