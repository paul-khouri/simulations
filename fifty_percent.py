import random
import math

def run_sim():
    population = []
    pop_size = 10000
    for i in range(1,pop_size + 1):
        if i <= pop_size/2:
            population.append("M")
        else:
            population.append("F")
    count_instances(population, "M")
    return population



def count_instances(l, n):
    count = 0
    for x in l:
        if x == n:
            count+=1
    output = "There are {} instances of {} in the list".format(count, n)
    #print(output)
    return count



def select_sample(p, s):
    temp = []
    temp = temp + p
    sample_size = s
    sample =[]
    for i in range(0,sample_size):
        choice = random.choice(temp)
        temp.remove(choice)
        sample.append(choice)
    return sample

def run_sim_and_write(p):
    set_proportions=[]
    writeFile = open("simulation.csv", "w")
    write_line = "{} , {}, {}\n".format("Trial", "Proportion", "Decile")
    writeFile.write(write_line)
    for i in range(0,1000):
        sample = select_sample(p, 343)
        count_m = count_instances(sample, "M")
        prop = count_m / 343
        set_proportions.append(prop)
    set_proportions.sort()
    for i in range(0, len(set_proportions)):
        prop = set_proportions[i]
        dec = math.floor(i/100)
        write_line ="{} , {}, {}\n".format(i+1, prop, dec+1)
        writeFile.write(write_line)
    writeFile.close()
    dist=get_distribution(set_proportions)
    print(dist)


def get_distribution(s):
    print(type(s))
    s.sort()
    deciles=[]
    for i in range(1, 10):
        index = math.floor(i*len(s)/10)
        print(index)
        deciles.append(s[index])
    k = 0
    for j in deciles:
        count = 0
        while s[k] <= j:
            if s[k] == j:
                output = "{} = {}".format(s[k], j)
                print(output)

            k += 1
            count+= 1
        output ="There are {} values below {}".format(count, j)
        print(output)


    return deciles


    print(len(s))
    print(s[0])
    print(s[-1])




# generate population
population = run_sim()
run_sim_and_write(population)





