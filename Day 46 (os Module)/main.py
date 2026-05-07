import os

if (os.path.exists("data")):
    os.mkdir("Day 46 (os Module)/data")

for i in range(1, 100):
    os.mkdir(f"Day 46 (os Module)/data/Day {i}")