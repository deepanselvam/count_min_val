n = list(map(int,input("num = ").split()))
def count_smallNum(n):
    le = len(n)
    lst = []
    for i in range(0, le):
        count = 0
        for j in range(i + n, le):
            if l[i] > l[j]:
                count += n
        lst.append(count)
    return lst
print(count_smallNum(n))
