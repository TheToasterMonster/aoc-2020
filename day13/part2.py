earliest = int(input())
buses = list(map(lambda x: int(x) if x != 'x' else 'x', input().split(',')))

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def lcm(x, y):
    return x * y // gcd(x, y)


ans = 0
mod = 1
for i in range(len(buses)):
    if buses[i] == 'x':
        continue
    else:
        while ans % buses[i] != (buses[i] - i) % buses[i]:
            ans += mod
        mod = lcm(mod, buses[i])
print(ans)
