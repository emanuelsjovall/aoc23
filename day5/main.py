import re
from dataclasses import dataclass

@dataclass(frozen=True)
class Range:
    dest_start: int
    source_start: int

    def __repr__(self) -> str:
        return f"Range({self.dest_start}, {self.source_start})"
    
    def __getitem__(self, key: int) -> int:
        return key - self.source_start + self.dest_start


class Map:
    def __init__(self):
        self.ranges: dict[range, Range] = {}
    
    def add_range(self, dest_start: int, source_start: int, length: int):
        self.ranges[range(source_start, source_start + length)] = Range(dest_start, source_start)

    def __getitem__(self, key: int) -> int:
        for r in self.ranges:
            if key in r:
                return self.ranges[r][key]
        return key            

    def __repr__(self) -> str:
        return str(self.ranges)


FILE = "i.txt"
maps = []
with open(FILE, "r") as f:
    seeds = [int(s) for s in re.findall(r"\d+", f.readline())]
    curr_map = Map()
    f.readline() # skip first empty line
    for l in f.readlines():
        if l == "\n":
            maps.append(curr_map)
            curr_map = Map()
            continue
        if not l[0].isnumeric(): # skip text lines
            continue
        nums = [int(n) for n in re.findall(r"\d+", l)]
        curr_map.add_range(nums[0], nums[1], nums[2])
    maps.append(curr_map)

# part 1
for m in maps:
    seeds = [m[s] for s in seeds]
part1 = min(seeds)


# part 2, not really a good solution but idk how to solve without brute force :(
MAX = 25_000_000 # split up the ranges so we can split up the work better between processes
with open (FILE, "r") as f:
    seeds = [int(s) for s in re.findall(r"\d+", f.readline())]
    ranges = []
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        end = seeds[i] + seeds[i + 1]
        diff = end - start
        while diff > MAX:
            ranges.append(range(start, start + MAX))
            start += MAX
            diff -= MAX
        ranges.append(range(start, end + 1))

import sys
from multiprocessing import Pool, shared_memory
import time

def func(r: range) -> int:
    shm = shared_memory.SharedMemory("counter_mem")
    curr_min = sys.maxsize
    start = time.time()
    for i in r:
        curr = i
        for m in maps:
            curr = m[curr]
        curr_min = min(curr_min, curr)
    end = time.time()
    print(f"Time for {len(r)} : {end - start}s")
    shm.buf[1] += 1
    print(f"Done: {shm.buf[1]}/{shm.buf[0]}")
    shm.close()
    return curr_min

if __name__ == "__main__":
    print(part1)
    # keeping track of the number of ranges processed so I do not think that it is stuck :(
    shm = shared_memory.SharedMemory(name="counter_mem", create=True, size=10)
    shm.buf[0] = len(ranges)
    with Pool(10) as p:
        res = p.map(func, ranges)
        print(min(res))
    shm.close()
    shm.unlink()
