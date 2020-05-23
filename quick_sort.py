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


def q_sort(seq):
    if len(seq) <=1:
        return seq
    pivot = seq[0]
    pivot_count = 0
    left_seq = []
    right_seq =[]
    for ele in seq:
        if ele < pivot:
            left_seq.append(ele)
        elif ele > pivot:
            right_seq.append(ele)
        else:
            pivot_count += 1

    left_seq = q_sort(left_seq)
    right_seq = q_sort(right_seq)

    return left_seq + [pivot] * pivot_count + right_seq


N = int(lines[0])
A_N = [int(x.strip()) for x in lines[1].split(' ')]
axis_index = (N-1)//2

A_N = q_sort(A_N)
#print(A_N)
print(' '.join(map(str, A_N)))
