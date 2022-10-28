import random
import copy
from collections import OrderedDict


def run_vote(vote, n):
    votes = []
    for i in range(0, n):
        voting_paper = vote.copy()
        keys = random.sample(list(voting_paper.keys()), k=random.randint(4, len(voting_paper)))
        for j in range(0, len(keys)):
            voting_paper[keys[j]] = j+1
        if random.random() < 0.25:
            swap_key_values(voting_paper, "B")
        votes.append(voting_paper)
    return votes


def votes_csv(f, votes):
    write_file = open(f, "w")
    header_list = []
    for k, v in votes[0].items():
        header_list.append(k)
    header_string = " ," + ','.join(header_list)+'\n'
    write_file.write(header_string)
    c = 1
    for v in votes:
        v_str = "{}".format(c)
        for k, val in v.items():
            v_str += ",{}".format(val)
        row = "{}\n".format(v_str)
        write_file.write(row)
        c += 1
    write_file.close()
    return None


def swap_key_values(vote, specified_key):
    # find the key with value=1
    # give that value to a specified key and
    # give the key with value 1 the specified key value
    key_one = ""
    for k, v in vote.items():
        if v == 1:
            key_one = k
    spec_key_value = vote[specified_key]
    vote[key_one] = spec_key_value
    vote[specified_key] = 1
    return None


if __name__ == "__main__":
    num_candidates = 15
    num_votes = 150
    start = ord('A')
    voting_paper = {}
    for i in range(start, start+num_candidates):
        voting_paper[chr(i)] = None
    file_name = "set_150_votes_8_candidates_biased.csv"
    votes = run_vote(voting_paper, num_votes)
    for x in votes:
        print(x)
    votes_csv(file_name, votes)
