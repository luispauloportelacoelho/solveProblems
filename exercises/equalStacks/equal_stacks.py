def equalStacks(h1, h2, h3):
    '''Remove values from stacks in order to have the same sum for both
    stacks.
    '''
    #
    # Write your code here.
    #
    h1_sum = sum(h1)
    h2_sum = sum(h2)
    h3_sum = sum(h3)

    h1 = h1[::-1]
    h2 = h2[::-1]
    h3 = h3[::-1]

    while not(h1_sum == h2_sum and h2_sum == h3_sum):
        if h1_sum > h2_sum or h1_sum > h3_sum:
            h1_sum = h1_sum - h1[-1]
            h1.pop()
        elif h2_sum > h1_sum or h2_sum > h3_sum:
            h2_sum = h2_sum - h2[-1]
            h2.pop()
        elif h3_sum > h1_sum or h3_sum > h2_sum:
            h3_sum = h3_sum - h3[-1]
            h3.pop()

    return h1_sum
