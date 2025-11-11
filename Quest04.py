def getText(day: str, part: int) -> str:
    folder = "inputs/"
    day_str = "{:02d}".format(day)  # adds leading zero if needed, s.t. we always have a 2 digit string
    name = folder + "everybody_codes_e2025_q" + day_str + "_p" + str(part) + ".txt"
    with open(name) as f:
        text = f.read() # .strip().split("\n")
    return text

def ceil(x):
    return int(- ((-x) // 1))  # Pythons // is a floor-div, so this is a ceil

# Part 1
text = getText(4,1)
number_teeth_str = text.split("\n")
first_number_teeth = int(number_teeth_str[0])
last_number_teeth = int(number_teeth_str[-1])
last_gear_full_cycles = ( 2025 * first_number_teeth ) // last_number_teeth
print(f"Part 1: {last_gear_full_cycles}")


# Part 2
text = getText(4,2)
number_teeth_str = text.split("\n")
first_number_teeth = int(number_teeth_str[0])
last_number_teeth = int(number_teeth_str[-1])
min_turns = 10000000000000
first_gear_needed_full_cycles = ceil((min_turns * last_number_teeth) / first_number_teeth)
print(f"Part 2: {first_gear_needed_full_cycles}")

# Part 3
text = getText(4,3)
lines = text.split("\n")
first_gear = int(lines[0])
last_gear = int(lines[-1])
rotations = 100
from_gear = first_gear
for line in lines[1:-1]:
    values = line.split("|")
    to_gear = int(values[0])
    rotations *= from_gear / to_gear
    from_gear = int(values[1])
rotations *= from_gear / last_gear
full_rotations = int(rotations)
print(f"Part 3: {full_rotations}")
