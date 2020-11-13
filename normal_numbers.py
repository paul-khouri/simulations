import numpy as np
import matplotlib.pyplot as plt
import math

mu , sigma = 0, 1
print(mu)

s= np.random.normal(mu, sigma, 10000)
# for i in s:
#     print(i)
# create bins
min_ =-4
max_ = 4
int_ =0.25
num_intervals_ = math.ceil((max_ - min_)/int_)+1
bin_list = []
for i in range(0,num_intervals_):
    x = min_ + i*int_
    bin_list.append(x)

count, bins , ignored = plt.hist(s, bin_list, density =True, facecolor='g', alpha=1)

min_ =-3
max_ = 3
int_ =0.01
num_intervals_ = math.floor((max_ - min_)/int_)
x_list=[]
for i in range(0,num_intervals_):
    x = min_ + i*int_
    x_list.append(x)

x_values=np.array(x_list)
print(bins)
print(count)
sum_c = 0
for c in count:
    sum_c += c
    #print(sum_c)
print(sum_c)
print(len(bins))
print(len(count))

#print(ignored)
plt.plot(x_values, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (x_values- mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
plt.axis([-6, 6, 0, 5])
plt.xlim(-6, 6)
plt.ylim(0, 1)
plt.grid(True)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(0, .025, r'$\mu=100,\ \sigma=15$')
plt.show()
