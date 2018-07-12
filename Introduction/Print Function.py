from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())

for x in range(1, n + 1):
    print(x, end="")

print(*range(1, n + 1), sep="")


# python3
# print(*range(1, int(input())+1), sep='')
