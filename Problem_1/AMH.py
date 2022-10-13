from time import time
from DATA import ReadFile as rf


S=[]
def moore(data):
    task_removed=[]
    concurrent_time=0
    a = sorted(data,key=lambda x: x[2],reverse=False)
    for i in range (0,len(data)):
            S.append(a[i])
            concurrent_time+=a[i][1]
            if (concurrent_time>  a[i][2]):
                index=max(S,key=lambda item: item[1])
                concurrent_time-=index[1]
                task_removed.append(index)
                S.remove(index)

    for i in range(len(task_removed)):
        task_removed_jobs=task_removed[i][0]
    num=len(task_removed)
    sequence=[]
    for i in range(0,len(S)):
        sequence.append(S[i][0])
    sequence.append(task_removed_jobs)

    return num,sequence

print("Enter the number of jobs to test (10 | 50 | 200 | 500):")
n = input()
data=rf.getData(n)
start=time()
a,b=moore(data)
print('The total number of late jobs:',a,)
print("The optimal sequence is:",b)
print("The runtime of the program is:",time()-start)