import sys
if __name__ == '__main__':
    ls = []
    ts = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        t = []
        t.append(name)
        t.append(score)
        ls.append(t)
        ts.append(score)
    mn = min(ts)
    m = sys.float_info.max
    for k in ls:
        if k[1] != mn:
            if k[1] < m:
                m = k[1]
    names = []
    for k in ls:
        if k[1] == m:
            names.append(k[0])
    names.sort()
    for s in names:
        print(s)
