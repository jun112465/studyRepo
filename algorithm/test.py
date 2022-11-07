import random

A = [random.randrange(1,101) for _ in range(10)]

cnt = 0
for i in range(len(A)):
    idx = A.index(min(A[i:]))
    A[i],A[idx] = A[idx], A[i]
    cnt += 1

print(A)
print(cnt)

