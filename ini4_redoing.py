'''
http://rosalind.info/problems/ini4/
Conditions and Loops

Given: Two positive integers aa and bb (a < b < 10000).

Return: The sum of all ODD integers from a through b, inclusively.


'''

file = open('ini4_data.txt', 'r').readline().split()

a = int(file[0])
b = int(file[1])

if a % 2 == 0: # If a is even, add 1 to make it odd
    a += 1


sum1 = 0 # Initialize the summer

while a <= b:    
    sum1 += a # Increment count plus a
    a += 2 # Increment a by two


print(sum1)

