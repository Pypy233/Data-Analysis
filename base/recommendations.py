from math import sqrt
def  euclidDistance(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in person2:
            si[item] = 1

    if len(si) == 0:    return 0

    sumOfSquares = sum([pow(prefs[person1][item] - prefs[person2][item], 2) for item in prefs[person1] if item in prefs[person2]])

    return 1/(1 + sqrt(sumOfSquares))


def pearsonDistance(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    if len(si) == 1:    return 1

    sum1 = sum([prefs[person1][item] for item in si])
    sum2 = sum([prefs[person2][item] for item in si])

    squareSum1 = pow(sum([prefs[person1][item] for item in si]), 2)
    squareSum2 = pow(sum([prefs[person2][item] for item in si]), 2)


    pearsonSum = sum([prefs[person1][item]*prefs[person2][item] for item in si])

    num = pearsonSum - (sum1 * sum2 / len(si))


    den = sqrt(squareSum1 - pow(sum1, 2) / len(si)) + sqrt(squareSum2 - pow(sum2, 2))

    if den == 0:
        return 0
    return num / den


def topMatches(prefs, person, n=5, similarity = pearsonDistance()):
    scores = [similarity(prefs, person, other) for other in prefs if person != other]
    scores.sort();
    scores.remove();
    return scores[0:n]