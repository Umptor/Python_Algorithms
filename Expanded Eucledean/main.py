import tabulate

def exp_eucledean(a, b):
    table = []
    if b == 0:
        d = a
        x = 1
        y = 0
        return(x, y)
    x1 = 0
    x2 = 1
    y1 = 1
    y2 = 0
    n = 0
    row = [0, '', '', '', '', a, b, x1, x2, y1, y2]
    table.append(row)
    while b > 0:
        q = (a - (a % b)) / b
        r = a % b
        x = q*x1 + x2
        y = q * y1 + y2

        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
        n += 1
        row = [n, q, r, x, y, a, b, x1, x2, y1, y2]
        table.append(row)

    d = a
    x = pow(-1, n) * x2
    y = pow(-1, n+1) * y2
    result = [[d, x, y]]
    return table, result

table, result = exp_eucledean(899, 3)
headers = ['n', 'q', 'r', 'x', 'y', 'a', 'b', 'x1', 'x2', 'y1', 'y2']
tableShow = tabulate.tabulate(table, headers)
print(tableShow)
print('')
tables_result = tabulate.tabulate(result, ['d', 'x', 'y'])
print(tables_result)
