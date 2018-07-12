#!/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
if N % 2 == 1:
    print "Weird"
elif N >= 6 and N <= 20:
    print "Weird"
else:
    print "Not Weird"

#####

N = int(raw_input())
if N % 2 == 1:
    print "Weird"
elif N in range(6, 21):
    print "Weird"
else:
    print "Not Weird"

########