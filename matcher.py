def find_best_match(students, mentors):
    best_match = None

    for mentor in mentors:
        for student in students:
            if student["interest"] == mentor["interest"]:
                best_match = mentor
                return best_match

    return mentors[0] #in case of fail