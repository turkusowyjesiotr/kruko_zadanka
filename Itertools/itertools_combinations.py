# https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true


from itertools import combinations

s, k = input().split()
s = sorted(s)
k = int(k)
answer = []

for i in range(1, k+ 1):
    comb = list(combinations(s, int(i)))
    comb = [''.join(i) for i in comb]
    for combination in comb:
        answer.append(combination)

for result in answer:
    print(result)