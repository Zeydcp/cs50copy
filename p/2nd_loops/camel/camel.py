snake_case = input('camelCase: ')
for c in snake_case:
    if c.isupper():
        snake_case = snake_case.replace(c, '_' + c.lower())
print('snake_case:', snake_case)