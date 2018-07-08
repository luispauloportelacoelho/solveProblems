class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.age = initialAge
        if initialAge < 0:
            print('Age is not valid, setting age to 0.')


    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            message = 'You are young.'
        elif self.age >= 18:
            message = 'You are old.'
        else:
            message = 'You are a teenager.'
            
        print(message)

    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1
        return self.age
t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
