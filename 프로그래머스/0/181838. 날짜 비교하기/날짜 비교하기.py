def solution(date1, date2):
    year1, month1, day1 = date1[0], date1[1], date1[2]
    year2, month2, day2 = date2[0], date2[1], date2[2]
    
    if year1 < year2:
        return 1
    elif year1 > year2:
        return 0
    else: # year1 == year2
        if month1 < month2:
            return 1
        elif month1 > month2:
            return 0
        else: # month1 == month2
            if day1 < day2:
                return 1
            elif day1 >= day2:
                return 0
            
    
