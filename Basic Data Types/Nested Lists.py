arr = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    arr.append([name, score])

print arr

sec_highest = sorted(list(set([marks for name, marks in arr])))[0]

print sec_highest

