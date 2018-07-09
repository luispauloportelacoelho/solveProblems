def calculate_note(query_name, student_marks):
    return round((sum(student_marks[query_name]) / 3), 2)
