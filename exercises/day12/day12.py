class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        sizeScores = len(scores)
        calculateAverage = sum(scores) / sizeScores

        if calculateAverage >= 90 and calculateAverage <= 100:
            return "O"
        elif calculateAverage >= 80 and calculateAverage < 90:
            return "E"
        elif calculateAverage >= 70 and calculateAverage < 80:
            return "A"
        elif calculateAverage >= 55 and calculateAverage < 70:
            return "P"
        elif calculateAverage >= 40 and calculateAverage < 55:
            return "D"
        elif calculateAverage < 40:
            return "T"



    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]


numScores = int(input()) # not needed for Python

scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade: ", s.calculate())
