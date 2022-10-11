# link : https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true

"""
문제 풀이
    player 리스트가 이미 정렬된 상태이기 때문에 
    이 성질을 이용해 랭크를 정할 때 매번 반복문을 통해 랭크를 찾는 것이 아니라
    이전 player의 랭크부터 검색을 시작하면 O(n)의 시간복잡도로 랭크를 정할 수 있게된다.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    answer = []
    ranked = list(set(ranked))
    ranked.sort(reverse = True)
    
    r = len(ranked)-1
    p = 0
    while r >= 0:
        if player[p] < ranked[r]:
            answer.append(r+2)
            p += 1
        elif player[p] == ranked[r]:
            answer.append(r+1)
            p += 1
        else:
            r -= 1
        if p == len(player):
            break
        
    while p < len(player):
        answer.append(1)
        p += 1
        
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
