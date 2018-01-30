'''
Counting Point Mutations


Given: Two DNA strings ss and tt of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)dH(s,t).
'''

file = open("dna6.txt", "r").readlines(0)

a = file[0].strip()
b = file[1].strip()


# Go through both strings and see if they match!

diffs = 0

for i in range(0,len(a)):
    if a[i] != b[i]:
        diffs += 1

print(diffs)
            
