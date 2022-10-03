
# https://www.hackerrank.com/challenges/no-idea/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n_m = input()
array = input().split()
set_A = set(input().split())
set_B = set(input().split())
happiness = 0

for i in array:
    if i in set_A:
        happiness += 1
    elif i in set_B:
        happiness -= 1

print(happiness)
