# # READING A FILE
# f = open('Day 49 (File IO)/myfile.txt', 'r')
# text = f.read()
# print(text)
# f.close()

# WRITING A FILE

# f = open('Day 49 (File IO)/myfile2.txt', 'a')
# f.write('Hello, world!\n')
# f.close()

# SECOND METHOD in Writing A File

with open('Day 49 (File IO)/myfile2.txt', 'a') as f:
    f.write("Hey I am Yash")