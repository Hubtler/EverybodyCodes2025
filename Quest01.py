def getText(day: str, part: int) -> str:
    folder = "inputs/"
    day_str = "{:02d}".format(day)  # adds leading zero if needed, s.t. we always have a 2 digit string
    name = folder + "everybody_codes_e2025_q" + day_str + "_p" + str(part) + ".txt"
    with open(name) as f:
        text = f.read() # .strip().split("\n")
    return text

def parse_to_lists(part: int)-> tuple[list[str],list[str]]:
    file_content = getText(1, part)
    content = file_content.split("\n\n")
    name_list = content[0].split(",")
    command_list = content[1].split(",")
    return name_list, command_list

def command_to_steps(command: str)-> int:
    direction = command[0]
    number_steps = int(command[1:])
    if direction == "L":
        number_steps *= -1
    return number_steps


# Part 1
name_list, command_list = parse_to_lists(1)

# command liste durchgehen
index:int = 0
last_index = len(name_list)-1
for command in command_list:
    number_steps = command_to_steps(command)
    index = max(0, min(last_index, index + number_steps) )

print(f"Your name is: {name_list[index]}")

# Part 2
name_list, command_list = parse_to_lists(2)

# command liste durchgehen
index = 0
for command in command_list:
    number_steps = command_to_steps(command)
    index += number_steps

index %= len(name_list)

print(f"One parent's name is: {name_list[index]}")


# Part 3
name_list, command_list = parse_to_lists(3)

# command liste durchgehen
index_list = list(range(len(name_list))) # list of valid indices
for command in command_list:
    number_steps = command_to_steps(command)
    index = number_steps % len(name_list)
    index_list[0], index_list[index] = index_list[index], index_list[0] # swap entries at indices: 0 and index

print(f"Second parent's name is: {name_list[index_list[0]]}")