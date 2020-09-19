import random
import math


def play_n_times(n):
    faces=["W","L"]
    h_count=0
    for i in range(0, n):
        face= random.choice(faces)
        if face=="W":
            h_count += 1
    return h_count

def run_sim(n):
    distribution = {}
    for i in range(0,n):
        count = play_n_times(32)
        if count in distribution.keys():
            distribution[count] += 1
        else:
            distribution[count] = 1
    distribution_items = distribution.items()
    sorted_ditribution = sorted(distribution_items)
    return sorted_ditribution

def write_out(d):
    writeFile = open("tamati_mia.csv", "w")
    write_line = "{} , {}\n".format("Number of wins", "Number of times it occurs")
    writeFile.write(write_line)
    for x in d:
        write_line=""
        for i in range(0, len(x)):
            if i != len(x)-1:
                write_line = "{}".format(x[i])
            else:
                write_line = "{},{}\n".format(write_line, x[i])
        writeFile.write(write_line)









#print(toss_coin_n_times(50))
result = run_sim(1000)
write_out(result)

