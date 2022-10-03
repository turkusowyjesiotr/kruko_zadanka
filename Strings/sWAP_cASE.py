# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true


def swap_case(s):
    result = ''
    for letter in s:
        if letter.islower():
            result += letter.upper()
        else:
            result += letter.lower()

    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)