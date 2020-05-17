import sys

def main(lines):
    for i, v in enumerate(lines):
        print("line[{0}]: {1}".format(i, v))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    #main(lines)

s = lines[0]
t = lines[1]

def createTable(pattern):
    table = [0 for _ in range(len(pattern))]
    j = 0
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
        else:
            table[i] = j
            j = 0
    return table #最後の値は使わない

def kmp(text,pattern):
    skip = createTable(pattern)

    t_len = len(text)
    p_len = len(pattern)
    t_i = p_i = 0

    while t_i < t_len and p_i < p_len:
        if text[t_i] == pattern[p_i]:
            t_i += 1
            p_i += 1
        elif p_i == 0:
            t_i += 1
        else:
            p_i = skip[(p_i)-1] #jump by skip
    if p_i == p_len:
        return t_i - p_i
    else:
        return -1
 
createTable(t)
result = kmp(s,t)
print(result)
