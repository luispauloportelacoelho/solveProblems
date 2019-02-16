from collections import Counter
def twoStacks(max_value: int, array_a: list, array_b: list) -> int:
    #
    # Write your code here.
    #
    array_a = array_a[::-1]
    array_b = array_b[::-1]

    array_a_sum = 0
    array_b_sum = 0
    count_moves = 0
    stack_a = []

    while array_a != []:
        if array_a_sum + array_a[-1] <= max_value:
            array_a_sum += array_a[-1]
            stack_a.append(array_a.pop())
            count_moves += 1
        else:
            break

    while array_b != []:
        if array_b_sum + array_b[-1] <= max_value:
            if array_a_sum + array_b[-1] <= max_value:
                array_a_sum += array_b[-1]
                array_b_sum += array_b[-1]
                array_b.pop()
                count_moves += 1
            else:
                array_a_sum += array_b[-1] - stack_a.pop()
                array_b_sum += array_b[-1]
                array_b.pop()
        else:
            break


    return count_moves
