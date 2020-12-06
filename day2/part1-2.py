import re

part1 = 0
part2 = 0

reg = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')

with open("./input.txt") as data:
    for d in data:

        g = reg.match(d).groups()
        low = int(g[0])
        high = int(g[1])
        c = g[2]
        word = g[3]

        if word.count(c) in range(low, high+1):
            part1 += 1
        if (word[low-1] == c and word[high-1] != c) or (word[low-1] != c and word[high-1] == c):
            part2 += 1

print("Part 1: ", part1)
print("Part 2: ", part2)