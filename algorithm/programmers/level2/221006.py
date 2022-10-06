# 문제링크
# https://school.programmers.co.kr/learn/courses/30/lessons/92335

from math import sqrt, floor

def isPrimeNumber(n):
    if n <= 1:
        return False
    
    for i in range(2,floor(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
        
def solution(n, k):
    answer = 0
    
    knum = ""
    while n > 0:
        knum = str(n%k) + knum
        n //= k
        
    
    numlist = [int(n) for n in knum.split('0') if n != '']
    for n in numlist:
        if isPrimeNumber(n):
            answer += 1

    return answer