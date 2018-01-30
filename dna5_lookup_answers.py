'''
http://rosalind.info/problems/gc/
Computing GC Content

Return: The ID of the string having the highest GC-content,
followed by the GC-content of that string. Rosalind allows
for a default error of 0.001 in all decimal answers unless
otherwise stated; please see the note on absolute error
below.


'''
file = open("dna5.txt", "r").read()

genes = file.split(">")[1:]

print(genes)

gc = []

for gene in genes:
    a = gene.count("C") + gene.count("G")
    b = gene.count("C") + gene.count("G") + gene.count("A") + gene.count("T")
    gc.append(float(a) * 100/b)

print(gc) # Print the list

print(genes[gc.index(max(gc))][:13])
print(max(gc))
