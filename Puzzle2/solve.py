def format_line(line):
    counts, letter, text = line.split(" ")
    min_count, max_count = [int(c) for c in counts.split("-")]
    letter = letter[0]  # remove :
    return text, letter, min_count, max_count


def verify_count(text, letter, min_count, max_count):
    actual_count = text.count(letter)

    return actual_count >= min_count and actual_count <= max_count


with open("input.txt", "r") as numbersfile:
    lineslist = numbersfile.readlines()

accumulator = 0
for l in lineslist:
    text, letter, min_count, max_count = format_line(l)
    accumulator += verify_count(text, letter, min_count, max_count)

print(accumulator)
