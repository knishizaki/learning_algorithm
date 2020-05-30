import sys

def main(lines):
    for i, v in enumerate(lines):
        print("line[{0}]: {1}".format(i, v))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    #main(lines)
N=int(lines[0])
A=[int(x.strip()) for x in lines[1].split(' ')]
A_max=max(A)
dp= [0]*(A_max+1)

for i in range(N): #列
    dp[A[i]]= max(dp[A[i]-1]+1, dp[A[i]])    

b_len=max(dp)
max_index = [i for i, v in enumerate(dp) if v == b_len]
begin_index = [i - b_len +1  for i in max_index]
#print(b_len, max_index,begin_index)

A_index=[]

for i in range(len(begin_index)):
    #print(A.index(begin_index[i]),begin_index[i])
    A_index.append(A.index(begin_index[i]))
#print(A_index)
min_A_index = A_index.index(min(A_index))
#print(min_A_index)

b_min = begin_index[min_A_index]
#print(b_min)

A_index_list=[]
for i in range(b_len):
    if i==0:
        A_index_added=A.index(b_min+i) #indexの捜索範囲を上げていかないといけない
    else:
        A_index_added=A[A_index_list[i-1]:].index(b_min+i) + A_index_list[i-1]
    A_index_list.append(A_index_added)
    #print(A_index_list[i])

result_list = [i+1 for i in A_index_list]

print(b_len)
print(' '.join(map(str, result_list)))
