import random
import math

def create_list(s):
    my_list = []
    for i in range(1, s+1):
        my_list.append(i)
    print(my_list)
    return my_list


def run_random(list_of_items):
    my_set = set()
    count = 0
    while len(my_set) < len(list_of_items):
        for i in range(0, 1):
            item = random.choice(list_of_items)
            my_set.add(item)
        count += 1
    return count

def run_sim(n):
    list = create_list(51)
    distribution = {}
    for i in range(0,n):
        count = run_random(list)
        if count in distribution.keys():
            distribution[count] += 1
        else:
            distribution[count] = 1
    distribution_items = distribution.items()
    sorted_ditribution = sorted(distribution_items)
    return sorted_ditribution

def write_out(d):
    writeFile = open("little_shop.csv", "w")
    write_line = "{} , {}\n".format("Number of visits to get set", "Number of times it occurs")
    writeFile.write(write_line)
    for x in d:
        write_line=""
        for i in range(0, len(x)):
            if i != len(x)-1:
                write_line = "{}".format(x[i])
            else:
                write_line = "{},{}\n".format(write_line, x[i])
        writeFile.write(write_line)

write_out(run_sim(10000))
