def getText(day: str, part: int) -> str:
    folder = "inputs/"
    day_str = "{:02d}".format(day)  # adds leading zero if needed, s.t. we always have a 2 digit string
    name = folder + "everybody_codes_e2025_q" + day_str + "_p" + str(part) + ".txt"
    with open(name) as f:
        text = f.read() # .strip().split("\n")
    return text

class Spine_row:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.next = None

    def get_number(self):
        number = ""
        if not self.left is None:
            number += str(self.left)
        number += str(self.value)
        if not self.right is None:
            number += str(self.right)
        return int(number)

class Sword:
    def __init__(self, identifier, fish_bone: Spine_row):
        self.id = identifier
        self.fish_bone = fish_bone
        self.quality = None

    def get_quality(self):
        if self.quality is None:
            quality = ""
            current_row = self.fish_bone
            while not current_row is None:
                quality += str(current_row.value)
                current_row = current_row.next
            self.quality = int(quality)
        return self.quality

    def __lt__(self, other):
        # returns true if self < other

        # If two swords have different qualities, a higher quality score means a better sword.
        if self.get_quality() != other.get_quality():
            return self.get_quality() < other.get_quality()

        # If the quality of both swords is the same,
        # the numbers resulting from the subsequent levels of the fishbone should be compared, starting from the top.
        # A higher score on the first level, which differs between swords, indicates a better sword.
        self_level = self.fish_bone
        other_level = other.fish_bone
        while not self_level is None and not other_level is None:
            self_score = self_level.get_number()
            other_score = other_level.get_number()
            if self_score != other_score:
                return self_score < other_score
            self_level = self_level.next
            other_level = other_level.next

        # If the above conditions are not met, the sword with the higher identifier is considered better.
        return self.id < other.id

def parse_sword(text):
    text_parts = text.split(":")
    identifier = int(text_parts[0])
    numbers = list(map(lambda x: int(x), text_parts[1].split(",")))
    top_spine_row = Spine_row(numbers[0])
    for number in numbers[1:]:
        current_row = top_spine_row
        last_checked_row = None
        placed = False
        while not current_row is None and not placed:
            if number < current_row.value and current_row.left is None:
                current_row.left = number
                placed = True
            elif number > current_row.value and current_row.right is None:
                current_row.right = number
                placed = True
            else:
                last_checked_row = current_row
                current_row = current_row.next
        if not placed:
            last_checked_row.next = Spine_row(number)
    return Sword(identifier, top_spine_row)

# Part 1
text = getText(5, 1)
sword = parse_sword(text)
print(f"Part 1: {sword.get_quality()}")

# Part 2
text = getText(5, 2)
lines = text.split("\n")
swords = [ parse_sword(line) for line in lines]
qualities = [sword.get_quality() for sword in swords]
max_quality = max(qualities)
min_quality = min(qualities)
difference = max_quality - min_quality
print(f"Part 2: {difference}")

# Part 3
text = getText(5, 3)
lines = text.split("\n")
swords = [ parse_sword(line) for line in lines]
sorted_swords = sorted(swords, reverse=True) # descending, from best to weakest
checksum = 0
for posmo, sword in enumerate(sorted_swords):
    checksum += (posmo+1) * sword.id
print(f"Part 3: {checksum}")