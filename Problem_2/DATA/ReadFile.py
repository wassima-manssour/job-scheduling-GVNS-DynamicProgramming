##DATA
#READ FROM A FILE   

def getData(n):

    file = open("Problem_2/DATA/P2_n"+n+".txt", "r")
    lines = file.readlines()
    
    jobs=[i+1 for i in range(int(lines[0]))]
    p=[int(i) for i in lines[1].split("\t")]
    d=[int(i) for i in lines[2].split("\t")]
    a=[int(i) for i in lines[3].split("\t")]
    b=[int(i) for i in lines[4].split("\t")]

    data = [[jobs[i],p[i],d[i],a[i],b[i]] for i in range(len(jobs))]
    print(data)

    n = len(data)
    print("Nombre de jobs=",n)

    return data                                                 
'''
print("Enter the number of jobs to test (10 | 100 | 200 | 500):")
n = input()
getData(n)
'''																