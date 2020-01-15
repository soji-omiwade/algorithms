import sys
x = int(sys.argv[1])

count = 0
while x != 0:
    count += (x%2)
    x //= 2

print(f"{count}")
