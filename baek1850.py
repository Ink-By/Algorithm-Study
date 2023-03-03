
def gcd_(a, b):
    if b == 0:
        return a
    else:
        return gcd_(b, a % b)


a, b = map(int, input().split())
print('1'*gcd_(a, b))
