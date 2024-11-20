import sys

def read_ballots(fname):
    with open(fname) as f:
        data = f.read().splitlines()
    f.close()
    ballots = []
    for datum in data:
        ballot = datum.split(",")
        ballots.append(ballot)
    return ballots

def find_candidates(ballots):
    candidates = []
    for ballot in ballots:
        for candidate in ballot:
            if candidate not in candidates:
                candidates.append(candidate)
    return candidates

def find_rank(cname,ballots):
    count = 0
    for ballot in ballots:
        if cname == ballot[0]:
            count = count + 1
    return count

def find_ranks(candidates,ballots):
    ranks = []
    for candidate in candidates:
        rank = find_rank(candidate,ballots)
        ranks.append((rank,candidate))
    return ranks

def find_candidates_with_least_first_place_votes(ranks):
    sorted_ranks = sorted(ranks)
    least_votes = sorted_ranks[0][0]
    result = []
    for rank in ranks:
        if rank[0] == least_votes:
            result.append(rank[1])
    return result

def eliminate_candidate_from_candidates(cname,candidates):
    result = []
    for candidate in candidates:
        if candidate != cname:
            result.append(candidate)
    return result

def eliminate_candidate_from_ballots(cname,ballots):
    result = []
    for ballot in ballots:
      if cname in ballot:
        ballot.remove(cname)
        if ballot != []:
            result.append(ballot)
    return result



def main ():
    #ballots = read_ballots(sys.argv[1])
    ballots = [
 ['Red','Green'],
 ['Blue'],
 ['Green','Red','Blue'],
 ['Blue','Green','Red'],
 ['Green']
]
    candidates = find_candidates(ballots)
    while True:
        # find candidates to eliminate
        ranks = find_ranks(candidates,ballots)
        candidates_to_eliminate = find_candidates_with_least_first_place_votes(ranks)

        # eliminate them
        for cname in candidates_to_eliminate:
            candidates = eliminate_candidate_from_candidates(cname,candidates)
            ballots = eliminate_candidate_from_ballots(cname,ballots)

        #check for winners
        if len(candidates) == 1:
            print("winner!", candidates[0])
            break
        elif len(candidates) == 0:
            print("loser")
            break

main()
