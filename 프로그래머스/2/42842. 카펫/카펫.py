def solution(brown, yellow):
    
    # 근의 공식으로 풀이
    a = 1
    b = -(brown-4)//2
    c = yellow
    
    Yx = (-b+(b**2-4*a*c)**(1/2)) // 2
    Yy = yellow // Yx
    
    return [Yx+2, Yy+2]
    
    
    # 예전 풀이
    # brown = (brown - 4) // 2
    # yellow_list = [i for i in range(1, brown) if i * (brown - i) == yellow]
    # return [max(yellow_list) + 2, min(yellow_list) + 2]