# https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true

from collections import deque
n = int(input())
for i in range(n):
    m = int(input())
    block = deque(map(int, input().split()))
    for j in range(m-1):
        if block[0] >= block[1] and block[0] >= block[-1]:
            block.popleft()
        elif block[-1] >= block[-2] and block[-1] >= block[0]:
            block.pop()
    if len(block) < 2:
        print('Yes')
    else:
        print('No')