import random


def run_vote(n):
    votes = []
    for i in range(0,n):
        voting_paper={
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None
        }
        keys = random.sample(list(voting_paper.keys()), k=random.randint(2,len(voting_paper)))
        for i in range(0,len(keys)):
            voting_paper[keys[i]]=i+1
        votes.append(voting_paper)
    return votes

def run_count_round(votes):
    bin = {
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "E": [],
        "F": []
    }
    for x in votes:
        vote = {i for i in x if x[i] == 1}
        bin[vote.pop()].append(x)
        # print(vote.pop())
    # print(bin)
    for x, y in bin.items():
        print("{} : {}".format(x,len(y)))
    return bin

def complete_round(bin, n):
    # find lowest number of votes
    # get those votes
    _min = n
    candidate = ""
    for x, y in bin.items():
        if len(y) <= _min:
            _min = len(y)
            candidate = x
    lowest_count_candidates = {i for i in bin if len(bin[i]) == _min}
    return lowest_count_candidates


n =20
votes = run_vote(n)
bin=run_count_round(votes)
lowest_count_candidates=complete_round(bin,n)
print(lowest_count_candidates)
#print(votes)







