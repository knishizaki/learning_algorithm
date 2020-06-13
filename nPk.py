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
def power(x, n):
    M = 10**9 + 7
    if n==0: return 1 # 0乗は1．
    tmp = power(x*x % M, n//2) # 再帰で計算
    if n%2: tmp = tmp * x % M # nが奇数の場合の処理
    return tmp

N=[int(x.strip()) for x in lines[0].split(' ')][0]
K=[int(x.strip()) for x in lines[0].split(' ')][1]
M= 10**9 + 7
#print(N,K)


n= N
p=1
while True:
   p = p*n
   n = n-1
   p = p % M
   if n <=0:
       break

n_k = N-K
p2 = 1 
while True:
    p2 = p2 * power(n_k, M-2)
    n_k = n_k -1
    #print(p2)
    p2 = p2 % M
    if n_k <= 0:
        break

calc = (p*p2)%M

print(calc)
