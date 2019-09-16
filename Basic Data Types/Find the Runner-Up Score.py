if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort(reverse=True)

    for x in range(n):
        if arr[x] != arr[x + 1]:
            print(arr[x + 1])
            break

#

# z = max(lis)
# while max(lis) == z:
#     lis.remove(max(lis))
#
# print max(lis)


#
# print sorted(list(set(nums)))[-2]
