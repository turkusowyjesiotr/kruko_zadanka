# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true


n = int(input())
s = set(map(int, input().split()))
count = int(input())
commands = []
for i in range(count):
    command = input().split()
    if len(command) == 2:
        command[1] = int(command[1])
    commands.append(command)


for j in commands:
    if j[0] == 'remove':
        s.remove(j[1])
    if j[0] == 'discard':
        s.discard(j[1])
    if j[0] == 'pop':
        if len(j) == 1:
            s.pop()
        else:
            s.pop(j[1])

print(sum(s))