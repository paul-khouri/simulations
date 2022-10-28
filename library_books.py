""" return 50 library books
4% chance of a book being late
find how many books are late
repeat n times for a distribution
"""
import random

def run_single_sim(n,p):
    late_books = 0
    for i in range(0, n):
        ran_num = random.random()
        if ran_num < p:
            late_books +=1

    #print(late_books)
    return late_books

def run_sim(n):
    distribution = {}
    for i in range(0,n):
        count = run_single_sim(50,0.04)
        if count in distribution.keys():
            distribution[count] += 1
        else:
            distribution[count] = 1
    distribution_items = distribution.items()
    sorted_ditribution = sorted(distribution_items)
    return sorted_ditribution

def write_out(d,n):
    print(d)
    writeFile = open("libary_test.csv", "w")
    write_line = "{} , {}, {}\n".format("Number of Late Books", "Number of times it occurs","Proportion")
    writeFile.write(write_line)
    for x in d:
        write_line=""
        for i in range(0, len(x)):
            if i != len(x)-1:
                write_line = "{}".format(x[i])
            else:
                write_line = "{},{},{:.10f}\n".format(write_line, x[i],x[i]/n)
        writeFile.write(write_line)

n = 1000000
result = run_sim(n)
write_out(result, n)