import random
import math


def toss_coin_n_times(n):
    faces=["H","T"]
    h_count=0
    toss_string = ""
    for i in range(0, n):
        face= random.choice(faces)
        toss_string += face+" "
        if face=="H":
            h_count += 1
    print(toss_string)
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

def write_out(d):
    writeFile = open("heads_tails_test.csv", "w")
    write_line = "{} , {}\n".format("Number of heads", "Number of times it occurs")
    writeFile.write(write_line)
    for x in d:
        write_line=""
        for i in range(0, len(x)):
            if i != len(x)-1:
                write_line = "{}".format(x[i])
                print(write_line)
            else:
                write_line = "{},{}\n".format(write_line, x[i])
                print(write_line)
        writeFile.write(write_line)









print(toss_coin_n_times(50))
#result = run_sim(3)
#write_out(result)

