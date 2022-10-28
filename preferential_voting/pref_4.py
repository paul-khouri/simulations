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


def votes_csv(f, header_list, votes, a=False):
    if a:
        writeFile = open(f, "a")
    else:
        writeFile = open(f, "w")

    header_string = " ," + ','.join(header_list)+'\n'
    writeFile.write(header_string)
    c = 1
    for v in votes:
        str = "{}".format(c)
        for k,val in v.items():
            str += ",{}".format(val)
        row = "{}\n".format(str)
        writeFile.write(row)
        c += 1


    writeFile.close()
    return None

def stats_csv(f,table):
    writeFile = open(f, "a")
    writeFile.write('\n')
    for row in table:
        writeFile.write(','.join(str(e) for e in row) + '\n')
    writeFile.close()
    return None


def run_count_round(bin_base,votes, available_candidates,i ,n):
    """Runs a complete recount at any voting round

    :param bin_base: dict
    :param votes: list
    :param available_candidates: list
    :param i: int
    :param n: into
    :return: bool, dict
    """
    winner = None
    bin_temp =copy.deepcopy(bin_base)
    # loop through each vote
    for v in votes:
        key, _min = get_min_available_keys(v, available_candidates[i], n)
        # get the best preference using available candidates
        if key in bin_temp:
            bin_temp[key].append(v)
        else:
            # some votes will have none for all available candidates
            # loop back through previous available candidates lists and find the last time their vote was used
            # attach to that candidate who will be an eliminated candidate
            c = 1
            while key is None:
                key, _min = get_min_available_keys(v, available_candidates[i-c], n)
                c += 1
            bin_temp[key].append(v)
    for x, y in bin_temp.items():
        print("{} : {}".format(x,len(y)))
        if len(y) > n/2:
            winner = "The winner is {} with {} votes".format(x,len(y))
    if winner is not None:
        print(winner)
        return True, bin_temp
    else:
        return False, bin_temp

def get_bin_stats(f,bin):
    header=["A","B","C","D","E", "F"]
    col = [1,2,3,4,5,6]
    table=[]
    temp = [""]
    for x in header:
       temp.append(x)
    table.append(temp)
    for y in col:
        temp=[y]
        for z in header:
            temp.append(0)
        table.append(temp)
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
    for k, v in stats.items():
        # get col postion for candidate
        tab_col= table[0].index(k)
        for key , value in OrderedDict( sorted(v.items()) ).items():
            # find preference row in table
            tab_row = find_row(table, key)
            #print("p: {} , c: {}".format(key, value), end="")
            # add value (which is the count of the number of votes belonging
            # a candidate with that preference level)
            table[tab_row][tab_col] = value
    #print_lists_as_table(table)
    stats_csv(f, table)


    print_lists_as_table(tanspose_table(table))


def find_row(table, val):
    for l in table:
        row=l
        if row[0] == val:
            return table.index(row)


def print_lists_as_table(table):
    for row in table:
        print(' '.join("{:3}".format(str(e)) for e in row))

def tanspose_table(table):
    row = len(table)
    col = len(table[0])
    for x in table:
        if len(x) != col:
            print("table is not rectangular")
            return None
    new_table= []
    for c in range(0,col):
        temp = []
        for r in range(0,row):
            temp.append(table[r][c])
        new_table.append(temp)
    return new_table

    return None





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
# will contain a list of all votes attached to that candidate
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
# all candidates available at the start
# each set of available candidates will be stored in avaialable candidates
available_candidates.append(temp)
# run the vote
# random allocation of preferences and number of preferences
n =100
votes = run_vote(voting_paper,n)
f = "vote_file.csv"
votes_csv(f,temp, votes)
bins=[]
output= "Voting total: {} votes".format(n)
print(output)
result = False
for i in range(0,50):
    output = "Starting Round {}".format(i+1)
    print(output)

    if result is not True and len(available_candidates[i])>=2:
        result, bin = run_count_round(bin_base, votes, available_candidates, i, n)
        bins.append(bin)
        get_bin_stats(f,bins[i])
        lowest_count_candidates=complete_round(bins[i],n, available_candidates[i])
        output = "The following lowest count candidate(s) have been removed: {} ".format(','.join(lowest_count_candidates))
        print(output)
        temp = [e for e in available_candidates[i] if e not in lowest_count_candidates]
        output = "Candidates for the next round are: {}".format(','.join(temp))
        print(output)
        available_candidates.append(temp)
    else:
        if result:
            print("Have majority")
        else:
            print("No Majority")

        break
    print("-"*30)
    # check for winner

#print(votes)







