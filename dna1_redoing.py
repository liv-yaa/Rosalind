'''
Given: A DNA string ss of length at most 1000 nt.

Return: Four integers (separated by spaces) counting
the respective number of times that the symbols 'A', 'C', 'G', and 'T'
occur in ss.



'''


file = open('dna1.txt', 'r').readline()


print(file)


a = 0
c = 0
g = 0
t = 0

for i in file:
    if i == 'A':
        a += 1
    elif i == 'C':
        c += 1
    elif i == 'G':
        g += 1
    elif i == 'T':
        t += 1

print(a, c, g, t)
