import re
with open("i.txt", "r") as f:
    # [0] is str of winning nums and [1] is str of your ticket nums
    lines: list[tuple[str, str]] = [line.strip().split(": ")[1].split(" | ") for line in f.readlines()]

# Part 1
res = 0
for l in lines:
    winning_nums = [int(n) for n in re.findall(r"\d+", l[0])]
    your_nums = [int(n) for n in re.findall(r"\d+", l[1])]
    nums = 0
    for n in your_nums:
        if n in winning_nums:
            nums += 1
    res += 1 * (2 ** (nums - 1)) if nums > 0 else 0
print(res)


# part 2 
cards = [1 for _ in range(0, len(lines))]
for i in range(0, len(cards)):
    winning_nums = set([int(n) for n in re.findall(r"\d+", lines[i][0])])
    your_nums = set([int(n) for n in re.findall(r"\d+", lines[i][1])])
    nums = len(winning_nums & your_nums) # works because all numbers on a scratch card are unique
    for n in range(1, nums + 1):
        cards[i + n] += 1 * cards[i]
print(sum(cards))


# old part 2
# cards = {i: 1 for i in range(0, len(lines))}
# for k, v in cards.items():
#     # process each card as many times as we have cards, O(n^99) time complexity lmao
#     for i in range(0, v):
#         winning_nums = [int(n) for n in re.findall(r"\d+", lines[k][0])]       
#         your_nums = [int(n) for n in re.findall(r"\d+", lines[k][1])]
#         nums = 0
#         for n in your_nums:
#             if n in winning_nums:
#                 nums += 1
#         for i in range(1, nums + 1):
#             if not k + i in cards:
#                 continue
#             cards[k + i] += 1
# print(sum(cards.values()))    # 5921508