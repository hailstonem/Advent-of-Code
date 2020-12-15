import numpy as np


def line_to_bool(line):
    return [x == "#" for x in line.strip("\n")]


def move_until_limit(coords=None, limits=(323, None), move=(1, 3)):
    if coords == None:
        coords = [(0, 0)]
    # Recursive move: easily adaptable to arbitrary decision: but could do this analytically
    next_move = [c + m for c, m in zip(coords[-1], move)]

    # print([(c, c_lim) for c, c_lim in zip(next_move, limits)])
    if all([c_lim is None or c < c_lim for c, c_lim in zip(next_move, limits)]):
        #    # print(next_move)
        coords.append(next_move)
        coords = move_until_limit(coords, limits, move)

    return coords


def remap_out_of_range_coords(coords=[(0, 0)], limits=[None, 32]):
    def safe_modulo(x, m):
        if m is None:
            return x
        else:
            return x % m

    return [[safe_modulo(x, limits[0]), safe_modulo(y, limits[1])] for x, y in coords]


with open("input.txt", "r") as numbersfile:
    lineslist = numbersfile.readlines()

np_map = np.array([line_to_bool(l) for l in lineslist])

# move through map:
moves = move_until_limit(limits=[np_map.shape[0], None])
moves = remap_out_of_range_coords(moves, limits=[None, np_map.shape[1]])

# get sum over moves
total_trees = np.sum((np_map[tuple(zip(*moves))]))
print(f"Total trees: {total_trees}")

"""----Part 2---"""
