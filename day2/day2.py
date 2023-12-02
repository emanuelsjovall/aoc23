import re

with open("i.txt", "r") as f:
    lines = [l.strip().split(": ")[1] for l in f.readlines()]

# part 1
have = {"red": 12, "green": 13, "blue": 14}
res = 0
for i in range(len(lines)):
    cubes: list[str] = re.findall(r"\d+\s(?:red|green|blue)", lines[i])
    valid = True
    for c in cubes:
        amount, color = c.split(" ") # "3 blue"
        if int(amount) > have[color]:
            valid = False
            break
    if valid:
        res += i + 1
print(res)

# part 2
res = 0
for l in lines:
    seen = {"red": 0, "green": 0, "blue": 0}
    cubes: list[str] = re.findall(r"\d+\s(?:red|green|blue)", l)
    for c in cubes:
        amount, color = c.split(" ")
        seen[color] = max(seen[color], int(amount))
    res += seen["red"] * seen["green"] * seen["blue"]
print(res)