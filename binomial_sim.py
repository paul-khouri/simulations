import random
import numpy as np
import matplotlib.pyplot as plt

def run_one_set(p, trials):
    c=0
    successes = 0
    while c < trials:
        my_random= random.random()
        if my_random<p:
            successes += 1
        c += 1
    #print(successes)
    return successes

def run_sim(p,trials, n):
    distribution = {}
    for i in range(0,n):
        count = run_one_set(p,trials)
        if count in distribution.keys():
            distribution[count] += 1
        else:
            distribution[count] = 1
    distribution_items = distribution.items()
    sorted_ditribution = sorted(distribution_items)
    return sorted_ditribution

def create_plot(sorted_dist):
    r = 0
    g = 0
    b = 0.7
    x_bar=[]
    y_val = []
    max_y = 0
    for x in sorted_dist:
        x_bar.append(x[0])
        y_val.append(x[1])
        if x[1] > max_y:
            max_y = x[1]

    plt.bar(x_bar, y_val, align='center', color=(r, g, b), alpha=1.0, width=0.9)
    ax = plt.gca()
    # print(ax)
    ax.set_xlim([0,300])
    ax.set_ylim([0, max_y])
    ax.set_axisbelow(True)
    plt.grid(color='green', linestyle='--', linewidth=0.5)
    plt.savefig('bar_plot.pdf')
    plt.show()




if __name__ == "__main__":
    #run_one_set(1/3, 300)
    final_distribution = run_sim(1/3, 300, 1000)
    create_plot(final_distribution)
    # x_bar=[1,2,3]
    # y_val=[45,10,69]
    # r = 0
    # g = 0
    # b = 0
    # plt.xticks([1,2,3])
    # plt.yticks([10, 20, 30,40,50,60,70,80])
    # plt.bar(x_bar, y_val, align='center', color=(r, g, b), alpha=0.5, width=0.9)
    # ax = plt.gca()
    # print(ax)
    # ax.set_xlim([-10,20])
    # ax.set_ylim([0, 200])
    # plt.savefig('bar_plot.pdf')
    # plt.show()

