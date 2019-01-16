import numpy as np
from time import time


def solve_grid(grid_):
    grid = grid_.copy()
    indices = list(zip(*np.where(grid == 0)))

    def is_valid_candidate(i, j):
        i0, i1 = i // 3 * 3, i // 3 * 3 + 3
        j0, j1 = j // 3 * 3, j // 3 * 3 + 3
        n = grid[i, j]
        if (grid[i] == n).sum() == 1 and (grid[:, j] == n).sum() == 1 and (grid[i0:i1, j0:j1] == n).sum() == 1:
            return True
        return False

    k = 0
    while (grid == 0).any():
        found = False
        idx = indices[k]
        for n in range(max(1, grid[idx]), 10):
            grid[idx] = n
            found = is_valid_candidate(*idx)
            if found:
                break
        if found:
            k += 1
        else:
            grid[idx] = 0
            while True:
                k -= 1
                idx = indices[k]
                if grid[idx] == 9:
                    grid[idx] = 0
                else:
                    grid[idx] += 1
                    break
    # print(grid)
    return int(''.join(map(str, grid[0, :3])))


def main():
    with open('p096_sudoku.txt', 'r') as f:
        file = f.readlines()

    k = 10
    n = len(file)
    start, end = 0, k
    grids = []
    while start != n:
        grid = np.zeros((9, 9), dtype='uint8')
        for i, line in enumerate(file[start + 1:end]):
            grid[i] = list(map(int, line.strip()))
        grids.append(grid)
        start, end = end, end + k

    T0 = time()
    S = 0
    for i, grid in enumerate(grids):
        print('grid {}'.format(i), end=' ')
        t0 = time()
        S += solve_grid(grid)
        print('time elapsed: {:.2f} sec'.format(time() - t0))
    print('total time elapsed: {:.2f} sec'.format(time() - T0))
    return S

if __name__ == '__main__':
    print(main())
