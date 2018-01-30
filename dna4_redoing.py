'''
http://rosalind.info/problems/fib/
Rabbits and Recurrence Relations

Given: Positive integers n ≤ 40 and k ≤ 5.

Return: The total number of rabbit pairs that
will be present after n months, if we begin
with 1 pair and in each generation, every pair
of reproduction-age rabbits produces a litter
of k rabbit pairs (instead of only 1 pair).

'''

file = open('dna4.txt', 'r').readline().split()


n, k = int(file[0]), int(file[-1])
print(n, k)


memo = {0:0, 1:1}
def fib(n):


    if not n in memo:
        memo[n] = fib(n - 1) + k * fib(n - 2)
    return memo[n]

print("Memo dict fib")
print(fib(file))





