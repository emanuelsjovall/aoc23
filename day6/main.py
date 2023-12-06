import re
with open("e.txt", "r") as f:
    times = [int(t) for t in re.findall(r"\d+", f.readline())]
    dists = [int(d) for d in re.findall(r"\d+", f.readline())]

# part: 1
res = 1
for i in range(0, len(times)):
    possible = 0
    for t in range(1, times[i]):
        if t * (times[i] - t) > dists[i]:
            possible += 1
    res *= possible
print(res)
    

# part: 2
res = 0
time = int("".join([str(i) for i in times]))
dist = int("".join([str(d) for d in dists]))
for t in range(1, time):
    if t * (time - t) > dist:
        res += 1
print(res)

# note, if input was larger it would probably be better to use some sort of modifed binary search to find the answers but since the input is small enought we can get away with just looping