def getText(day: str, part: int) -> str:
    folder = "inputs/"
    day_str = "{:02d}".format(day)  # adds leading zero if needed, s.t. we always have a 2 digit string
    name = folder + "everybody_codes_e2025_q" + day_str + "_p" + str(part) + ".txt"
    with open(name) as f:
        text = f.read() # .strip().split("\n")
    return text

# Part 1
text = getText(3,1)
numbers = map( lambda x: int(x), text.split(",") )
numbers_unique = set(numbers)
size = sum(numbers_unique)
print(f"Part 1: {size}")

# Part 2
text = getText(3,2)
numbers = map( lambda x: int(x), text.split(",") )
numbers_unique = set(numbers)
numbers_sorted = sorted(numbers_unique) # ascending by default
size = sum(numbers_sorted[:20])
print(f"Part 2: {size}")

# Part 3
text = getText(3,3)
numbers = map( lambda x: int(x), text.split(",") )
number_count = {}
for number in numbers:
    if number in number_count:
        number_count[ number ] += 1
    else:
        number_count[ number ] = 1
number_sets_needed = max(number_count.values())
print(f"Part 3: {number_sets_needed}")