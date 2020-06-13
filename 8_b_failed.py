import sys

def main(lines):
    for i, v in enumerate(lines):
        print("line[{0}]: {1}".format(i, v))

def prime(n): #素数判定
    if n <= 1: False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

def prime_all(n):
    # is_prime[i]がTrue -> iが素数．
    is_prime = [True]*(n+1)
    is_prime[0]=is_prime[1]= False
    i = 2
    while i*i<= n:
        if prime(i)==True:
            s = 2
            while i*s <=n:
                is_prime[i*s] = False   
                s += 1
        i += 1
    return is_prime

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    #main(lines)

Q =int(lines[0])
l_r= [None]*Q
for i in range(Q):
    l_r[i]=[int(x.strip()) for x in lines[i+1].split(' ')]
#print(l_r)

max_n=[]
for i in range(Q):
    max_n.append(l_r[i][1])
max_n_value=max(max_n)
n = max_n_value
#print(n)
#print(prime_all(n)) #素数リスト完成
is_prime = prime_all(n)
p = 0
for p in range(Q):
    o = (l_r[p][0]+1)//2
    u = (l_r[p][1]+1)//2
    k = o
    counts = 0 
    while k<=u:
        s = 2*k-1
        if is_prime[k]== True and is_prime[s] == False:
            counts += 1      
        k+= 1
    print(len([i for i in range(o, u+1) if is_prime[i]])-counts)

