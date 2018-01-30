'''
http://rosalind.info/problems/ini3/
Strings and Lists

Given: A string ss of length at most 200 letters and
four integers aa, bb, cc and dd.

Return: The slice of this string from indices aa through
bb and cc through dd (with space in between), inclusively.
In other words, we should include elements s[b]s[b] and
s[d]s[d] in our slice.

'''

file = open('ini3_data.txt', 'r').readlines()
# Reads a string file into a list of strings

words = file[0] # The string that needs to be split
nums = file[-1].split() # The slice indices a:b, c:d, inclusive, sep by " "

# Convert strings to integers so they can be used for slicing
a = int(nums[0])
b = int(nums[1])
c = int(nums[2])
d = int(nums[3])

print(words[a:(b + 1)] + " " + words[c:(d + 1)])
