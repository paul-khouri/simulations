import random
import math


def toss_coin_n_times(n):
    faces=["H","T"]
    h_count=0
    for i in range(0, n):
        face= random.choice(faces)
        if face=="H":
            h_count += 1
    return h_count

def random_n_times(n):
    choice_count=0
    for i in range(0, n):
        my_random = random.random()

        if my_random < 0.128:
            choice_count += 1

    return choice_count

def run_random_sim(n=1000):
    distribution = {}
    for i in range(0,n):
        count = random_n_times(13500)
        if count in distribution.keys():
            distribution[count] += 1
        else:
            distribution[count] = 1
    distribution_items = distribution.items()
    sorted_distribution = sorted(distribution_items)
    return sorted_distribution

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
    writeFile = open("PioneerAttendance.csv", "w")
    write_line = "{} , {}\n".format("Number people", "Number of times it occurs")
    writeFile.write(write_line)
    for x in d:
        write_line=""
        for i in range(0, len(x)):
            if i != len(x)-1:
                write_line = "{}".format(x[i])
                #print(write_line)
            else:
                write_line = "{},{}\n".format(write_line, x[i])
                #print(write_line)
        writeFile.write(write_line)









#print(toss_coin_n_times(50))
#result = run_sim(3)
#write_out(result)

result=run_random_sim()
write_out(result)


