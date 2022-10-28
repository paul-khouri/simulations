import random
import copy
import csv
from collections import OrderedDict



def csv_file_reader(f):
    """Read a file of individual votes
    each vote is a dictionary with the key = candidate name and value = preference
    votes are collected in a list.
    A bin dictionary with key candidate and value = empty list also created

    :param f: str
    :return: list , dict
    """
    collected_votes = []
    candidates = []
    bin_base = {}
    #x = None if x == 'None' else x
    with open(f , mode='r', encoding='utf-8-sig') as csv_file:
        csv_read = csv.reader(csv_file, delimiter = "," , quotechar='"', quoting=csv.QUOTE_MINIMAL)
        count = 0
        for row in csv_read:
            if count == 0:
                candidates = row
            else:
                temp_vote = {}
                for i in range(1, len(row)):
                    bin_base[candidates[i]] = []
                    if row[i] == 'None':
                        temp_vote[candidates[i]] = None
                    else:
                        temp_vote[candidates[i]] = int(row[i])
                collected_votes.append(temp_vote)
            count += 1
    print(count)
    return collected_votes, bin_base

def get_min_available_keys(d, keys, n):
    """Check a single vote and find lowest pref number
    from the avaalable candidates in the lst (keys)
    Can return None

    :param d: dict
    :param keys: list
    :param n: int
    :return: str or None , int
    """
    _min = n
    key = None
    #print(d)
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
    for row in table:
        writeFile.write(','.join(str(e) for e in row) + '\n')
    writeFile.write('\n')
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
    # create a fresh bin
    bin_temp =copy.deepcopy(bin_base)
    # loop through each vote
    for v in votes:
        # get the best preference using available candidates
        # can get a None return if vote has chosen None for all of the available candidates
        key, _min = get_min_available_keys(v, available_candidates[i], len(bin_base))
       # if we get an actual preference
        if key in bin_temp:
            bin_temp[key].append(v)
        else:
            # some votes will have none for all available candidates
            # loop back through previous available candidates lists and find the last time their vote was used
            # attach to that candidate who will be an eliminated candidate
            # this will create some residuals
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

def get_bin_stats(f,bin, header):
    col=[]
    for i in range(0,len(header)):
        col.append(i+1)
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




def run_vote_from_csv(bin_base, votes_list):
    """Run the whole vote process

    :param bin_base: dict
    :param votes_list: list
    :return: None
    """

    # will store available candidates for each voting round
    # previous rounds are stored if backtracking needed
    available_candidates = []
    # first set of available candidates (all)
    temp=[]
    for x, y in bin_base.items():
        temp.append(x)
    available_candidates.append(temp)
    # container for the bins from each voting round
    all_bins = []
    f = "vote_summary_file.csv"
    # create fresh file
    open(f, "w")
    n= len(votes_list)
    result = False
    for i in range(0,50):

        # if no majority and 2 or more candidates
        if result is not True and len(available_candidates[i])>=2:
            output = "Starting Round {}".format(i + 1)
            print(output)
            # run the count
            result, bin = run_count_round(bin_base, votes_list, available_candidates, i, n)
            # collect latest bin
            all_bins.append(bin)
            # print stats for this voting round
            get_bin_stats(f,all_bins[i], available_candidates[0])
            # find candidate(s) to remove
            lowest_count_candidates=complete_round(all_bins[i],n, available_candidates[i])
            output = "The following lowest count candidate(s) have been removed: {} ".format(','.join(lowest_count_candidates))
            print(output)
            # create new list of available candidates with lowest removed
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
    return all_bins

def vote_pathway(v, all_bins):
    output = ""
    c = 1
    print(v)
    for b in all_bins:
        for candidate,votes in b.items():
            if v in votes:
                output += "In round {} the vote was associated with candidate {}\n".format(c, candidate)
        c += 1
    print(output)


        # gets dict with list values





if __name__ == "__main__":
    read_file = "set_of_100_votes.csv"
    collected_votes, bin_base = csv_file_reader(read_file)
    for x in collected_votes:
        print(x)
    # print(bin_base)
    all_bins = run_vote_from_csv(bin_base, collected_votes)
    print(len(all_bins))
    vote = {'A': 1, 'B': None, 'C': 2, 'D': None, 'E': None, 'F': 3}
    vote = {'A': None, 'B': 2, 'C': None, 'D': None, 'E': 1, 'F': None}
    vote = {'A': 1, 'B': None, 'C': None, 'D': None, 'E': None, 'F': 2}
    vote = {'A': None, 'B': 4, 'C': 5, 'D': 3, 'E': 2, 'F': 1}
    vote_pathway(vote, all_bins)










