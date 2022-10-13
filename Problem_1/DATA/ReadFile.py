##DATA
#READ FROM A FILE   

def getData(n):

    file = open("Problem_1/DATA/P1_n"+n+".txt", "r")
    lines = file.readlines()
    10
    jobs=[i+1 for i in range(int(lines[0]))]
    p=[int(i) for i in lines[1].split("\t")]
    d=[int(i) for i in lines[2].split("\t")]

    data = [[jobs[i],p[i],d[i]] for i in range(len(jobs))]
    print(data)

    n = len(data)
    print("Number of jobs=",n)

    return data                                                 

'''
print("Enter the number of jobs to test (10 | 50 | 200 | 500):")
n = input()
getData(n)
'''