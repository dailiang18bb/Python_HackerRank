from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

print a // b  # "//" is integer division, which return a integer
print a / b  # "/" is float division, which return a float

##python3

# a, b = int(input()), int(input())
# print(a // b, a / b, sep= '\n' )


##

print("{0}\n{1}".format(a // b, a / b))

##
