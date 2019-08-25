import random

alphabet = [
  'A', 'B', 'C', 'D', 'E', 'F',
  'G', 'H', 'I', 'J', 'K', 'L',
  'M', 'N', 'O', 'P', 'Q', 'R',
  'S', 'T', 'U', 'V', 'W', 'X',
  'Y', 'Z'
]

low_range = 0
high_range = 25


def shift_value(low, high):
    val = random.randrange(low, high)
    return val


def encrypt(char):
    pass


my_message = "z a"

shift_int = shift_value(low_range, high_range)
print(f'this is the shift {shift_int}')

for elem in my_message:
    if elem != ' ':
        location_as_int = alphabet.index(elem.upper())
        shift_location = location_as_int + shift_int
        adjusted_result = shift_location - high_range
        result = adjusted_result
    else:
        result = ''
    print(result)
