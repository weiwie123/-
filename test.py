def fenzu(lis):
    n = len(lis)
    mid = n // 2
    lis1 = lis[:mid]
    lis2 = lis[mid:]
    return merge(lis1, lis2)

def merge(lis1, lis2):
    new_lis = []
    l, r = 0, 0
    n1 = len(lis1)
    n2 = len(lis2)
    while l < n1 and r < n2:
        if lis1[l] < lis2[r]:
            new_lis.append(lis1[l])
            l += 1
        else:
            new_lis.append(lis2[r])
            r += 1
    new_lis.extend(lis1[l:])
    new_lis.extend(lis2[r:])
    return new_lis

lis = [9,3,2,4,5,5,5]
fenzu(lis)
lis