'''
http://rosalind.info/problems/ini2/
Variables & Some Arithmetic

Given: Two positive integers aa and bb, each less than 1000.

Return: The integer corresponding to the square of the hypotenuse
of the right triangle whose legs have lengths aa and bb.

Sample dataset: 3 5
Sample output: 34

'''

file = open('ini2_data.txt', 'r').readline().split()

print(file)




from math import sqrt

def arith(f):
    a, b = int(f[0]), int(f[-1])

    print(a)
    print(b)
    return ((a ** 2 )+ (b ** 2))

print(arith(file))

