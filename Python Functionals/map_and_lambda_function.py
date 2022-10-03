# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true

cube = lambda x: x**3 # complete the lambda function

def fibonacci(n):
    fib = [0, 1]
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        for i in range(n - 2):
            i = fib[-1] + fib[-2]
            fib.append(i)
        return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))