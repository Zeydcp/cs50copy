vowels = ['a', 'e', 'i', 'o', 'u']
output = input('Input: ')
for c in output:
    if c.lower() in vowels:
        output = output.replace(c, '')
print('Output:', output)