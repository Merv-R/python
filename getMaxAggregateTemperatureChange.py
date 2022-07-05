import sys

def getMaxAggregateTemperatureChange(tempChange):
    r_sum = sum(tempChange)
    l_sum = 0
    res = -sys.maxsize  # float("-inf")
    for i in tempChange:
        l_sum += i
        result = max(res, l_sum, r_sum)
        r_sum -= i
    return result


tempChange = [6,-2,5]
