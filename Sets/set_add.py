# https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

n = int(input())
stamps = []
for i in range(n):
    stamps.append(input())

stamps = set(stamps)
print(len(stamps))