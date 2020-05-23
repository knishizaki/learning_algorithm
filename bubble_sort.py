import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    for i, v in enumerate(lines):
        print("line[{0}]: {1}".format(i, v))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    #main(lines)

A_index = int(lines[0])-1
A_i = [int(x.strip()) for x in lines[1].split(' ')]

def bubble_sort(A,x):
    A_index = int(lines[0])-1
    for i in range(x-1):
        #if A_i[A_index-i] >= A_i[A_index- i -1]:
        #    break
        #    print("交換せず")
            #print("交換せず",A_index-i)
        if A_i[A_index-i] < A_i[A_index-i-1]:
            smaller = A_i[A_index-i]
            bigger = A_i[A_index-(i+1)]
            A_i[A_index-(i+1)] = smaller
            A_i[A_index-i] = bigger
            #print(A_i)
            #print("交換",A_index-i)
        #else:
            #print("どちらでもない",A_index-i)
        # print("A_index=",A_index-i,A_index-i-1,i)
   # print(A_i)

    return



#print(A_i)
x = int(lines[0])
while x >0:
    bubble_sort(A_i,x)
#    print(x)
    x += -1

print(' '.join(map(str,A_i)))
