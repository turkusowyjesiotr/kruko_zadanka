# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    stuart_score, kevin_score = 0, 0
    length = len(string)
    for i in range(length):
        score = length - i
        if string[i] in vowels:
            kevin_score += score
        else:
            stuart_score += score
    if stuart_score == kevin_score:
        print('Draw')
    if stuart_score > kevin_score:
        print(f'Stuart {stuart_score}')
    if stuart_score < kevin_score:
        print(f'Kevin {kevin_score}')


if __name__ == '__main__':
    s = input()
    minion_game(s)