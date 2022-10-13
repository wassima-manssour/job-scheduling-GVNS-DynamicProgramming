In this project we study the single-machine scheduling problem with two objectives: 

The first is to minimize the total number of tardy jobs, and the second is to minimize the total 
sum of the weighted earliness and tardiness for a set of independent jobs.

Giving n jobs to be processed for which each has an integer processing time pi and a due date 
di, the first problem denoted 1||∑Ui aims to minimize the number of late jobs, regardless of 
the amount of lateness. It can be solved optimally by the Moore-Hodgson algorithm (MHA). 
In addition to the MHA, we proposed a Dynamic Programming (DP) and a general variable 
neighborhood search (GVNS)algorithm to solve the problem.

As for the second problem denoted 1|| ∑αiEi+ βiTi, where αi and βi are respectively penalties 
on early and tardy jobs. The objective is to minimize the total Weighted Earliness and 
Tardiness by using DP and GVNS.

By comparing the results obtained by each of the exact and approach methods, it is shown 
that for large sets of jobs, the proposed GVNS algorithm can provide better solutions within 
a reasonable running time.