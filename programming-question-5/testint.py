def determinable(t, ints):
    for i in ints:
        if ints.get(t - i):
            return True
    return False

ints = dict([(int(i), True) for i in open('HashInt.txt').readlines()])
print(''.join([str(int(determinable(t, ints))) for t in [231552,234756,596873,648219,726312,981237,988331,1277361,1283379]]))

