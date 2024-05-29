from collections import namedtuple

Interval = namedtuple('Interval', ['l', 'r'])

n = int(input())

intervals = set()
for _ in range(n):
    l, r = map(int, input().split())
    intervals.add(Interval(l, r))


schedule = set()

while intervals:
    champion_interval = min(intervals, key=lambda x: x.r)
    schedule.add(champion_interval)
    intervals.remove(champion_interval)

    new_intervals = intervals.copy()

    for interval in intervals:
        if interval.l <= champion_interval.r:
            new_intervals.remove(interval)

    intervals = new_intervals

print(len(schedule))
