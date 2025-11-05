def getText(day: str, part: int) -> str:
    folder = "inputs/"
    day_str = "{:02d}".format(day)  # adds leading zero if needed, s.t. we always have a 2 digit string
    name = folder + "everybody_codes_e2025_q" + day_str + "_p" + str(part) + ".txt"
    with open(name) as f:
        text = f.read() # .strip().split("\n")
    return text

def get_A(part):
    text = getText(2, part)
    text = text[3:-1]  # remove "A=[" and "]
    A_str = text.split(",")
    A = complexNumber(int(A_str[0]), int(A_str[1]))
    return A

class complexNumber:
    def __init__(self, re: int, im: int):
        self.re = re
        self.im = im

    def __add__(self, other):
        return complexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return complexNumber(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def __truediv__(self, other):
        return complexNumber(int(self.re / other.re), int(self.im / other.im))

    def __str__(self):
        return f"[{self.re},{self.im}]"

A = get_A(1)
d = complexNumber(10, 10)
R = complexNumber(0,0)
for i in range(3):
    R *= R
    R /= d
    R += A
print(f"Part 1: {R}")


# Part 2
def gets_engraved(p: complexNumber):
    d = complexNumber(100000,100000)
    R = complexNumber(0,0)
    for C in range(100):
        R *= R
        R /= d
        R += p
        if not ( -1000000 <= R.re <= 1000000 ) or not ( -1000000 <= R.im <= 1000000 ):
            return False
    return True

A = get_A(2)
grid_size = 101
corner_one_distance = 1000
step_size = corner_one_distance//(grid_size-1)
number_engraved_points = 0
the_range = range(0,corner_one_distance + step_size, step_size)  # range from 0 to corner_one_distance (including end) in grid_size-steps
#visualization = ""
for y in the_range:
    for x in the_range:
        p = A + complexNumber(x,y)
        if gets_engraved(p):
            number_engraved_points += 1
#            visualization += "xx"
#        else:
#            visualization += ".."
#    visualization += "\n"
print(f"Part 2: {number_engraved_points}")
#print(visualization)

# Part 3
A = get_A(3)
grid_size = 1001
corner_one_distance = 1000
step_size = corner_one_distance//(grid_size-1)
number_engraved_points = 0
the_range = range(0,corner_one_distance + step_size, step_size)  # range from 0 to corner_one_distance (including end) in grid_size-steps
#visualization = ""
for y in the_range:
    for x in the_range:
        p = A + complexNumber(x,y)
        if gets_engraved(p):
            number_engraved_points += 1
#            visualization += "xx"
#        else:
#            visualization += ".."
#    visualization += "\n"
print(f"Part 3: {number_engraved_points}")
#print(visualization)