# https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

from collections import Counter

k = int(input())
rooms = input().split()
c = Counter(rooms)
for k, v in c.items():
    if v == 1:
        print(k)