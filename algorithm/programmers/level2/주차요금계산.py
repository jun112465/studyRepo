'''
링크 : https://school.programmers.co.kr/learn/courses/30/lessons/92341
단순한 시뮬레이션 문제
'''

import math

def solution(fees, records):
    answer = []
    
    parse_record = dict()
    
    for r in records:
        tmp = r.split()
        if tmp[1] not in parse_record:
            parse_record[tmp[1]] = list()
        
        time = list(map(int, tmp[0].split(":")))
        parse_record[tmp[1]].append(time[0]*60 + time[1])
    
    
    keys = list(parse_record.keys())
    keys.sort()
    for key in keys:
        data = parse_record[key]
        if len(data)%2!=0:
            data.append(23*60 + 59)

        min = 0
        for i in range(0, len(data), 2):   
            min += data[i+1] - data[i]
        
        cost = fees[1]
        min -= fees[0]
        if min > 0:
            cost += fees[3] * math.ceil(min / fees[2])
        
        answer.append(cost)
            
    return answer