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
    if student.get("interest") == mentor.get("interest"):
        score += 3

    #major match
    if student.get("major") == mentor.get("major"):
        score += 2

    #language match
    if student.get("language") == mentor.get("language"):
        score += 2

    #year match
    if abs(student.get("year", 0) - mentor.get("year", 0)) <= 1:
        score += 1
    print("SCORE between", student["name"], "and", mentor["name"], "=", score)
    return score
