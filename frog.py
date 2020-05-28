import sys

def main(lines):
    for i, v in enumerate(lines):
        print("line[{0}]: {1}".format(i, v))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    #main(lines)

N = int(lines[0])
h = [int(x.strip()) for x in lines[1].split(' ')]
#print(h)
h.insert(0,0)
def min_sum(a):
    s = [0]*(len(a))
    s[1]=abs(h[2]-h[1])
    s[0]=0
    #print(h)
    for i in range(len(h)-3):
    #    print("i=",i)
        s[i+2]= min(s[i+1]+ abs(h[i+3]-h[i+2]),s[i] + abs(h[i+3]-h[i+1]))
    return s[N-1]

x =min_sum(h)
print(x)
