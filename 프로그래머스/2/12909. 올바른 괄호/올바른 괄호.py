def solution(s):
    s = list(s)
    temp = []
    
    if s[0] == ')' or s[-1] == '(':
        return False
    for elem in s:
        if elem == '(':
            temp.append(elem)
        else:
            try:
                temp.pop()
            except:
                return False
    if temp:
        return False
    return True
