import numpy as np
import matplotlib.pyplot as plt


def get_Poisson():
    dist = {}
    s = np.random.poisson(5, 10)
    for x in s:
        if x in dist:
            dist[x] += 1
        else:
            dist[x] = 1
        #print(x)
    #print(s)
    #print(type(s))
    # item[0] for key item[1] for value
    print({key: value for key, value in sorted(dist.items(), key=lambda item: item[0])})
    #print(dist)


    count, bins, ignored = plt.hist(s, 14, density=True)

    #plt.show()

get_Poisson()


