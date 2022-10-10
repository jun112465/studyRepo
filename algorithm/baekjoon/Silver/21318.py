# 누적합을 이용해 푸는 문제
# https://www.acmicpc.net/problem/21318
import sys

N = int(input())
levels = list(map(int, input().split()))
sum_cnt = [0]*N
for i in range(N-1):
    sum_cnt[i+1] = sum_cnt[i]+1 if levels[i] > levels[i+1] else sum_cnt[i]


Q = int(input())

for i in range(Q):
    # 1 ~ N
    x,y = map(int, sys.stdin.readline().split())
    print(sum_cnt[y-1] - sum_cnt[x-1])
