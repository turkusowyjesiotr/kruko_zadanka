# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

def merge_the_tools(string, k):
    while string:
        u = string[:k]
        string = string[k:]
        u = ''.join(sorted(set(u), key=u.index))
        print(u)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
