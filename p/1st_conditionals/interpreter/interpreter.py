import operator

expression = input('Expression: ')
x, y, z = expression.split(' ')
x, z = float(x), float(z)

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
}

result = ops[y](x, z)
print("{:.1f}".format(result))
