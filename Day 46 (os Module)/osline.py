import os

folders = os.listdir("Day 46 (os Module)/data")

# print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"Day 46 (os Module)/data/{folder}"))