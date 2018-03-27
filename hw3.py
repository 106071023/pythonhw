a = input('Please type anything:\n')
b = dict()
b = {}
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
for i, count in  b.items():
    print(i, count)
