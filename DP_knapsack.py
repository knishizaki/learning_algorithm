import sys

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
N=[int(x.strip()) for x in lines[0].split(' ')][0]
W_limit= [int(x.strip()) for x in lines[0].split(' ')][1]

A,w_list, v_list =[],[],[]
for i in range (N):
    A = [int(x.strip()) for x in lines[i+1].split(' ')]
    w_list.append(A[0])
    v_list.append(A[1])
#print(N, W_limit)
#print(w_list,v_list)

note = [[-1 for _ in range(W_limit+1)]for _ in range(len(v_list)+1)]
#print(note)

def knapsack():
    note[0] = [0] * (W_limit + 1)
    weight_sum = 0
    for i in range(N):
        for w in range(W_limit+1):
            if w_list[i]> w:
                note[i+1][w] = note[i][w]
            else:
                not_in = note[i][w]
                is_in=note[i][w-w_list[i]]+v_list[i]
                note[i+1][w] = max(not_in, is_in)
            #print(note)            
    return note[N][W_limit]

print(knapsack())
