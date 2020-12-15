def get_sum_2020_2n(numberslist):
    numberslist2020 = [2020 - x for x in numberslist]

    for x in numberslist:
        if x in numberslist2020:
            return x, 2020 - x


def get_sum_2020_3n(numberslist):
    numberslist2020 = [2020 - x for x in numberslist]

    for x in numberslist:
        residuals = [y - x for y in numberslist2020]
        # this allows for double use of numbers:
        for r in residuals:
            # only search if residual >0
            if r and r in numberslist:
                return r, x, 2020 - r - x


with open("numbers.txt", "r") as numbersfile:
    lineslist = numbersfile.readlines()


numberslist = [int(x) for x in lineslist]

x, y = get_sum_2020_2n(numberslist)
# multiply
print(f"2n result: {x * y}")

x, y, z = get_sum_2020_3n(numberslist)
# multiply
print(f"3n result: {x * y * z}")
