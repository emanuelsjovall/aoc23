import re
import heapq

with open("i.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

# Part 1
digits: list[list[str]] = [re.findall(r'[0-9]+', l) for l in lines]
res = 0
for ld in digits:
    res += int(ld[0][0] + ld[-1][-1])
print(res)

# Part 2
swap = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

res = 0
for line in lines:
    f, l = [], []
    nums = [n for n in "".join(re.findall(r'[0-9]+', line))] # make all the 456 into 4, 5, 6 
    for n in nums:
        heapq.heappush(f, (line.find(n), n))
        heapq.heappush(l, (-line.rfind(n), n))
    for k, v in swap.items():
        if k in line:
            heapq.heappush(f, (line.find(k), v))
            heapq.heappush(l, (-line.rfind(k), v))
    res += int(heapq.heappop(f)[-1] + heapq.heappop(l)[-1])
print(res)
