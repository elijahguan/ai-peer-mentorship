def find_best_match(student, mentors):
    best_match = None
    best_score = -1

    for mentor in mentors:
        score = score_match(student, mentor)
        if score > best_score:
            best_score = score
            best_match = mentor


    return best_match

def score_match(student, mentor):
    score = 0

    #interest match
    if student["interest"] == mentor["interest"]:
        score += 3

    #major match
    if student["major"] == mentor["major"]:
        score += 2

    #language match
    if student["language"] == mentor["language"]:
        score += 2

    #year match
    if abs(student["year"] - mentor["year"]) <= 1:
        score += 1

    return score
