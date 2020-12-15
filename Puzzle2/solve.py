def format_line(line):
    counts, letter, text = line.split(" ")
    min_count, max_count = [int(c) for c in counts.split("-")]
    letter = letter[0]  # remove :
    return text, letter, min_count, max_count


def verify_count(text, letter, min_count, max_count):
    actual_count = text.count(letter)

    return actual_count >= min_count and actual_count <= max_count


def verify_position(text, letter, pos1, pos2, count):
    true_positions = sum([text[pos1 - 1] == letter, text[pos2 - 1] == letter])
    return true_positions == count


with open("input.txt", "r") as numbersfile:
    lineslist = numbersfile.readlines()

accumulator = 0
for l in lineslist:
    text, letter, min_count, max_count = format_line(l)
    accumulator += verify_count(text, letter, min_count, max_count)
print(f"Part one: Matched: {accumulator}")

accumulator = 0
for l in lineslist:
    text, letter, pos1, pos2 = format_line(l)
    accumulator += verify_position(text, letter, pos1, pos2, 1)
print(f"Part two: Matched: {accumulator}")
