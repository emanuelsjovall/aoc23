graph: dict[str: tuple[str, str]] = {}
with open("i.txt") as f:
    dirs = f.readline().strip()
    f.readline()
    for line in f.readlines():
        line = line.strip().split(" = ")
        graph[line[0]] = (line[1][1:4], line[1][6:9])

# Part 1
node = "AAA"
steps = 0
while node != "ZZZ":
    dir = 0 if dirs[steps % len(dirs)] == "L" else 1
    node = graph[node][dir]
    steps += 1
print(steps)


# Part 2
nodes: list[str] = [k for k in graph if k[2] == "A"]
cycles: list[int] = []
# find how manys steps in the cycle to go from Start -> **Z -> whatever whereever -> **Z or whatnot
for n in nodes: 
    steps = 0
    node = n
    while node[2] != "Z":
        dir = 0 if dirs[steps % len(dirs)] == "L" else 1
        node = graph[node][dir]
        steps += 1
    cycles.append(steps)

from math import lcm
print(lcm(*cycles))