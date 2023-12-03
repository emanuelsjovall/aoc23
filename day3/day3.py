with open("i.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# part 1
import re
res = 0
for r in range(len(lines)):
    for c in range(len(lines[r])):
        char = lines[r][c]
        if char.isnumeric() or char == ".":
            continue
        # symbol
        seen_spans = set()
        for ro in range(-1, 2):
            for co in range(-1, 2):
                ri = r + ro
                ci = c + co
                if ri < 0 or ci < 0 or ri > len(lines) or ci > len(lines[r]):
                    continue
                for m in re.finditer(r"\d+", lines[ri]):
                    s = m.span()
                    ss = f"{ri}-{s[0]}-{s[1]}"
                    if ss not in seen_spans and ci in range(s[0], s[1]):
                        seen_spans.add(ss)
                        res += int(m.group())
print(res) 


# part 2
res = 0
for r in range(len(lines)):
    for c in range(len(lines[r])):
        char = lines[r][c]
        if char != "*":
            continue
        # * symbol
        seen_spans = set()
        nums = []
        for ro in range(-1, 2):
            for co in range(-1, 2):
                ri = r + ro
                ci = c + co
                if ri < 0 or ci < 0 or ri > len(lines) or ci > len(lines[r]):
                    continue
                for m in re.finditer(r"\d+", lines[ri]):
                    s = m.span()
                    ss = f"{ri}-{s[0]}-{s[1]}"
                    if ss not in seen_spans and ci in range(s[0], s[1]):
                        seen_spans.add(ss)
                        nums.append(int(m.group()))
        if len(nums) == 2:
            res += nums[0] * nums[1]
        nums = []
print(res)