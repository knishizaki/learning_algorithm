import sys

def main(lines):
    for i, v in enumerate(lines):
        print("line[{0}]: {1}".format(i, v))


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    #main(lines)

N=[int(x.strip()) for x in lines[0].split(' ')][0]
W_limit= [int(x.strip()) for x in lines[0].split(' ')][1]
V_max = N * 200
A,w_list, v_list =[],[],[]
for i in range (N):
    A = [int(x.strip()) for x in lines[i+1].split(' ')]
    w_list.append(A[0])
    v_list.append(A[1])

#print(N, W_limit)
#print(w_list,v_list)


dp = [[-1 for _ in range(V_max+1)]for _ in range(N+1)]

def knapsack():
    for i in range(N):
        dp[i][0]= 0
    for k in range(1,N+1):
        for j in range(V_max+1):
            if dp[k-1][j] ==-1 and dp[k-1][j-v_list[k-1]] != -1:
                dp[k][j] = dp[k-1][j-v_list[k-1]] + w_list[k-1]
            elif dp[k-1][j] != -1 and dp[k-1][j-v_list[k-1]] == -1:
                dp[k][j] = dp[k-1][j]
            else:
                dp[k][j] = min(dp[k-1][j-v_list[k-1]] + w_list[k-1], dp[k-1][j])
    search_w = W_limit
    l = dp[N]
    N_list = [0 if i > W_limit or i == -1 else 1 for i in l]
    max_index = max([i for i, x in enumerate(N_list) if x == 1])
    return max_index

print(knapsack())


