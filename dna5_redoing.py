'''
http://rosalind.info/problems/gc/
Computing GC Content

Return: The ID of the string having the highest GC-content,
followed by the GC-content of that string. Rosalind allows
for a default error of 0.001 in all decimal answers unless
otherwise stated; please see the note on absolute error
below.


'''
file = open("dna5.txt", "r").readlines()

stringa = ''
for i in file:
    stringa += i.strip()

stringb = stringa.split('>')
stringb.pop(0)
    

keys = []
values = []

for i in stringb:
    keys.append(i[0:13])
    values.append(i[14:])


# Make a dictionary to store the key:value pairs

dicta = dict(zip(keys, values))


# Compute GC content

gc_val = 0
total = 0

for key in dicta:
    for value in dicta[key]:
        gc_val += (value.count("C") + value.count("G"))
        total += (value.count("A") + value.count("T") + value.count("C") + value.count("G"))
        # Change the value to the CG% value
        dicta[key] = float(gc_val * 100 / total)


lista = []

for key, val in dicta.items():
    if val == max(dicta.values()):
        print(key)
        print(val)

