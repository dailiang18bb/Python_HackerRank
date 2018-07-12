if __name__ == '__main__':
    n = int(raw_input())

for x in range(n):
    print x ** 2

x = 0
while x in range(n):
    print x * x
    x = x + 1

# Python3
# [print(i**2) for i in range(n)]


# Python3
# print(*[num**2 for num in range(n)], sep='\n')
