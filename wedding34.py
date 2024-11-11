"""Wedding Module"""
from itertools import product


class Wedding:
    """Initialize the Wedding class"""

    def __init__(self):
        self.results = []

    def arrangements(self, guests):
        """Define a function to generate all possible arrangements of a list of guests"""
        if len(guests) == 1:
            return guests

        if len(guests) == 2:
            results = [guests, guests[1] + guests[0]]
            return results

        results = []
        for temp in self.arrangements(guests[1:]):
            results.append(guests[0] + temp)

        for temp in self.arrangements(guests[2:]):
            results.append(guests[1] + guests[0] + temp)

        return results

    def shuffle_procedure(self, guests):
        """Define a function to shuffle a list of guests."""
        results = []

        if len(guests) == 2:
            results = [guests, "".join(reversed(guests))]
            return results

        for temp in self.arrangements(guests[1:]):
            results.append(guests[0] + temp)

        for temp in self.arrangements(guests[2:]):
            results.append(guests[1] + guests[0] + temp)

        results.append(guests[-1] + guests[:-1])

        for temp in self.arrangements("".join(reversed(guests[1:-1]))):
            results.append(guests[-1] + "".join(reversed(temp)) + guests[0])

        results.append(guests[1:] + guests[0])

        return results

    def generate(self, results):
        """Define a function to generate all possible arrangements of a list of guests."""
        return list(product(*results))

    def barriers_procedure(self, guests, bars):
        """Define a function to generate all possible arrangements of guests with barriers."""
        barriers_result = []
        arrange_list = []
        temp = 0
        generate_results = []

        for bar in bars:
            if bar == 0:
                continue
            arrange_list.append(guests[temp:bar])
            temp = bar

        if temp != len(guests) and len(bars) != 0 and bars[0] != 0:
            arrange_list[0] = guests[temp:] + arrange_list[0]

        elif len(bars) == 1 and bars[0] == 0:
            barriers_result.append(self.arrangements(guests))
        elif len(bars) > 1 and bars[0] == 0:
            arrange_list.append(guests[temp:])

        for lst in arrange_list:
            barriers_result.append(self.arrangements(lst))

        gen_rest = self.generate(barriers_result)
        for temp_rest in gen_rest:
            if bars[0] == 0:
                temp_rest = "".join(temp_rest)
            else:
                temp_rest = "".join(temp_rest)
                temp_str1 = temp_rest[0:(len(guests) - bars[-1])]
                temp_str2 = temp_rest[(len(guests) - bars[-1]):]
                temp_rest = temp_str2 + temp_str1

            i = 0
            for bar in bars:
                temp_rest = temp_rest[0:bar + i] + "|" + temp_rest[bar + i:]
                i += 1

            generate_results.append(temp_rest)

        return generate_results

    def shuffle(self, guests):
        """Return shuffled arrangement of guests."""
        result = self.shuffle_procedure(guests)
        return result

    def barriers(self, guests, bars):
        """Return barriers for guest."""
        result = self.barriers_procedure(guests, bars)
        return result


def show_result(v, partial=False, ind=None):
    """Display the results"""
    v.sort()
    if not partial:
        print(len(v), "\n".join(v), sep="\n")
    else:
        print(len(v), v[ind], sep="\n")


def standard_tests():
    """Tests for Wedding Command"""
    standard = Wedding()
    res = standard.shuffle("abc")
    show_result(res)

    res = standard.shuffle("WXYZ")
    show_result(res)

    res = standard.barriers("xyz", [0])
    show_result(res)

    res = standard.shuffle("abcdefXY")
    show_result(res)

    res = standard.barriers("abcDEFxyz", [2, 5, 7])
    show_result(res)

    res = standard.barriers("ABCDef", [4])
    show_result(res)

    res = standard.barriers("bgywqa", [0, 1, 2, 4, 5])
    show_result(res)

    res = standard.barriers("n", [0])
    show_result(res)
    res = standard.shuffle("hi")
    show_result(res)


def main():
    """Main for user commands."""
    print(
        """Type quit to exit.
Commands:
tests
s guests
b guests n barriers
sp guests ind
bp guests n barriers ind
"""
    )
    w = Wedding()
    while True:
        asktype = input().split()
        if not asktype or asktype[0] == "quit":
            break
        if asktype[0] == "tests":
            standard_tests()
        elif asktype[0] == "s":
            guests = asktype[1]
            r = w.shuffle(guests)
            show_result(r)
        elif asktype[0] == "b":
            guests, bars = asktype[1], asktype[3:]
            r = w.barriers(guests, [int(x) for x in bars])
            show_result(r)
        elif asktype[0] == "sp":
            guests, ind = asktype[1:]
            r = w.shuffle(guests)
            show_result(r, True, int(ind))
        elif asktype[0] == "bp":
            guests, bars, ind = asktype[1], asktype[3:-1], asktype[-1]
            r = w.barriers(guests, [int(x) for x in bars])
            show_result(r, True, int(ind))


if __name__ == "__main__":
    main()
