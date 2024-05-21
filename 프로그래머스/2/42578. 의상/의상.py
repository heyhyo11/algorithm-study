def solution(clothes):
    box = {} 
    answer = 1
    
    for name, category in clothes:
        if category in box.keys():
            box[category] += [name]
        else:
            box[category] = [name]
    
    for value in box.values():
        answer *= (len(value) + 1)
        
    return answer -1