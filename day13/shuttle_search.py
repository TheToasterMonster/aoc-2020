earliest = int(input())
buses = input().split(',')
available_buses = []
for bus in buses:
    if bus != 'x':
        available_buses.append(int(bus))

times = dict(map(lambda x: (x - earliest % x, x), available_buses))
earliest_bus = min(times)
ans = earliest_bus * times[earliest_bus]
print(ans)
