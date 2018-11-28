def gridChallenge(grid: list) -> str:

    response = 'YES'

    len_grid = len(grid)
    len_inside_grid = len(grid[0])

    sort_local_grid = []
    counter = 0

    for x in range(0, len_grid):
        sort_local_grid.extend(sorted(grid[x]))

        if x > 0:
            for y in range(x*len_inside_grid, x*len_inside_grid + len_inside_grid):

                if sort_local_grid[counter] > sort_local_grid[y]:
                    return 'NO'

                counter += 1

    return response
