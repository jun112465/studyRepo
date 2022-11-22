from collections import deque

def solution(queue1, queue2):
    maxlen = len(queue1)*5
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    cnt = 0
    
    while True:
        # 1번 테스트케이스를 통과하기 위해서는 maxlen을 큰 값으로 줘야했다
        # 기존에는 len*2를 넣었었다.
        if cnt >= maxlen:
            return -1
        elif sum1 == sum2:
            return cnt
        elif sum1 > sum2:
            pop = queue1.popleft()
            queue2.append(pop)
            sum1 -= pop
            sum2 += pop
        else:
            pop = queue2.popleft()
            queue1.append(pop)
            sum1 += pop
            sum2 -= pop
        cnt += 1