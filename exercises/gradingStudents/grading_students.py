def gradingStudents(grades):
    #
    # Write your code here.
    #
    sizeGrades = len(grades)

    countLimit = 3
    newGrades = []

    for x in range(sizeGrades):

        count = 1

        calc = grades[x] % 10

        if calc == 0 or calc == 5 or calc == 1 or calc == 2 or calc == 6 or calc == 7 or grades[x] <= 37:
            print(grades[x])
            newGrades.append(grades[x])
        elif grades[x] > 37 and grades[x] <= 40:
            print(40)
            newGrades.append(40)
        else:

            if calc == 3:
                print(grades[x])
                newGrades.append(grades[x] + 2)

            elif calc == 4:
                print(grades[x])
                newGrades.append(grades[x] + 1)

            elif calc == 8:
                print(grades[x])
                newGrades.append(grades[x] + 2)

            elif calc == 9:
                print(grades[x])
                newGrades.append(grades[x] + 1)

    return newGrades


print(gradingStudents([73, 78, 60]))

print(0%10)
