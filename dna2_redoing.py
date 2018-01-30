'''
http://rosalind.info/problems/rna/
Transcribing DNA into RNA

Given: A DNA string tt having length at most 1000 nt.

Return: The transcribed RNA string of tt.

'''

file = open('dna2.txt', 'r').readline()

output = []

for i in range(0, len(file)):
    if file[i] != 'T':
        output.append(file[i])
    elif file[i] == 'T':
        output.append('U')

str_output = ''

for j in output:
    str_output += j

print(str_output)
    
        
