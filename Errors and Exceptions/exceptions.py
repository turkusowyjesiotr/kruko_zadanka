# https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

n = int(input())
for i in range(n):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except Exception as error:
        print(f'Error Code: {error}')