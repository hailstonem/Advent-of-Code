import numpy as np


def line_to_bool(line):
    return [x == "#" for x in line.strip("\n")]


def move_until_limit(coords=None, limits=(323, None), move=(1, 3)):
    if coords == None:
        coords = [(0, 0)]
    # Recursive move: easily adaptable to arbitrary decision: but could do this analytically
    next_move = [c + m for c, m in zip(coords[-1], move)]

    if all([c_lim is None or c < c_lim for c, c_lim in zip(next_move, limits)]):

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
# use of numpy array not really necessary: we could just step through each line:
# but it does allow us to precalculate all the positions and extract the tree presence easily
np_map = np.array([line_to_bool(l) for l in lineslist])

# move through map:
moves = move_until_limit(limits=[np_map.shape[0], None])
moves = remap_out_of_range_coords(moves, limits=[None, np_map.shape[1]])

# get sum over moves
total_trees = np.sum((np_map[tuple(zip(*moves))]))
print(f"Total trees: {total_trees}")

"""----Part 2---"""
# Now we can reuse that numpy map
# slopes are defined opposite of question brief
slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

trees_acc = np.int64(1)  # Large: Avoid overflow!
for slope in slopes:
    print(f"Slope: {slope}")
    moves = move_until_limit(limits=[np_map.shape[0], None], move=slope)
    print(moves[2])
    moves = remap_out_of_range_coords(moves, limits=[None, np_map.shape[1]])
    trees = np.sum((np_map[tuple(zip(*moves))]))
    print(trees)
    trees_acc = trees_acc * trees
print(f"Multiplied Trees: {trees_acc}")
