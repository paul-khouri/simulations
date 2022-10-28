import random
import math


def toss_coin_n_times(n):
    #print("Fifty coin tosses are about to happen")
    faces=["H","T"]
    h_count=0
    for i in range(0, n):
        face= random.choice(faces)
        #print(face, end="")
        if face=="H":
            h_count += 1
    output= "   There are {} heads".format(h_count)
    #print(output)

    return h_count

def run_sim(n):
    distribution = {}
    for i in range(0,n):
        count = toss_coin_n_times(50)
        if count in distribution.keys():
            distribution[count] += 1
        else:
            distribution[count] = 1
    distribution_items = distribution.items()
    sorted_ditribution = sorted(distribution_items)
    return sorted_ditribution

def write_out(d,n):
    print(d)
    writeFile = open("heads_tails_test.csv", "w")
    write_line = "{} , {}\n".format("Number of heads", "Number of times it occurs")
    writeFile.write(write_line)
    for x in d:
        write_line=""
        for i in range(0, len(x)):
            if i != len(x)-1:
                write_line = "{}".format(x[i])
            else:
                write_line = "{},{},{:.10f}\n".format(write_line, x[i],x[i]/n)
        writeFile.write(write_line)









#print(toss_coin_n_times(50))
n = 1000000
result = run_sim(n)
write_out(result, n)

