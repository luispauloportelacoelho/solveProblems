from collections import deque

def truckTour(petrolpumps):
    #
    # Write your code here.
    #

    #[[1, 5], [10, 3], [3, 4]]

    circular_queue = deque(petrolpumps)
    numberOfPoint = len(petrolpumps)
    dieselInTank = 0

    stops = 0
    nextStop = 0
    cycle = 0

    while stops != (numberOfPoint):

        dieselInTank += circular_queue[stops][0]

        dieselInTank -= nextStop

        nextStop = circular_queue[stops][1]
        stops += 1

        if nextStop > dieselInTank:
            dieselInTank = 0
            nextStop = 0
            stops = 0
            circular_queue.rotate(-1)
            cycle += 1

    return cycle
