'''
http://rosalind.info/problems/ini5/
Working with Files

Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines
from the original file. Assume 1-based numbering of lines.

'''

file = open("ini5_data.txt", "r").readlines()
# Open text file as a list of strings

output = ""

for i in range(0, len(file)): # Iterate through list of strings
    if i % 2 == 1:
        print(file[i])


