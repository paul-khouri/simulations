import random
import copy
from collections import OrderedDict

def get_min_available_keys(d, keys, n):
    _min = n
    key = None
    for x, y in d.items():
        if x in keys:
            if y is not None and y < _min:
                _min = y
                key = x
    #if key is None:
       # print("Problem")

    return key, _min


def run_vote(vote,n):
    votes = []
    for i in range(0,n):
        voting_paper = vote.copy()
        keys = random.sample(list(voting_paper.keys()), k=random.randint(2,len(voting_paper)))
        for i in range(0,len(keys)):
            voting_paper[keys[i]]=i+1
        votes.append(voting_paper)
    return votes


def run_count_round(bin_base,votes, available_candidates,i ,n):
    winner = None
    bin_temp =copy.deepcopy(bin_base)
    for d in votes:
        key, _min = get_min_available_keys(d, available_candidates[i], n)
        if key in bin_temp:
            bin_temp[key].append(d)
        else:
            c=1
            while key is None:
                key, _min = get_min_available_keys(d, available_candidates[i-c], n)
                c +=1
            bin_temp[key].append(d)
    for x, y in bin_temp.items():
        print("{} : {}".format(x,len(y)))
        if len(y) > n/2:
            winner = "The winner is {} with {} votes".format(x,len(y))
    if winner is not None:
        print(winner)
        return True, bin_temp
    else:
        return False, bin_temp

def get_bin_stats(bin):
    stats={}

    for x , y in bin.items():
        # each dictionary in the list
        candidate = {}
        for z in y:
            pref_num = z[x]
            if pref_num in candidate:
                candidate[pref_num] += 1
            else:
                candidate[pref_num] = 1
        stats[x]=candidate
    #print(stats)
    for x, y in stats.items():
        print("{}: ".format(x), end="")
        for key , value in OrderedDict( sorted(y.items()) ).items():
            print("p: {} , c: {}".format(key, value), end="")
            print(" -- ", end="")
        print()










def complete_round(bin, n,available_candidates):
    # find lowest number of votes
    # get those votes
    _min = n
    candidate = ""
    for x, y in bin.items():
        if x in available_candidates:
            if len(y) <= _min:
                _min = len(y)
                candidate = x
    lowest_count_candidates = {i for i in bin if len(bin[i]) == _min}
    return list(lowest_count_candidates)


voting_paper = {
    "A": None,
    "B": None,
    "C": None,
    "D": None,
    "E": None,
    "F": None
}
bin_base = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "E": [],
    "F": []
}
available_candidates = []
temp=[]
for x, y in voting_paper.items():
    temp.append(x)
available_candidates.append(temp)
n =500
votes = run_vote(voting_paper,n)
bins=[]
output= "Voting total: {} votes".format(500)
print(output)
for i in range(0,5):
    output = "Starting Round {}".format(i+1)
    print(output)
    result, bin = run_count_round(bin_base,votes,available_candidates,i,n)
    bins.append(bin)
    if result is not True and len(available_candidates[i])>2:
        get_bin_stats(bins[i])
        lowest_count_candidates=complete_round(bins[i],n, available_candidates[i])
        output = "The following lowest count candidate(s) have been removed: {} ".format(','.join(lowest_count_candidates))
        print(output)

        temp = [e for e in available_candidates[i] if e not in lowest_count_candidates]
        output = "Candidates for the next round are: {}".format(','.join(temp))
        print(output)
        available_candidates.append(temp)
    else:
        get_bin_stats(bins[i])
        break
    print("-"*30)
    # check for winner

#print(votes)







