import random

alphabet = [
  'A', 'B', 'C', 'D', 'E', 'F',
  'G', 'H', 'I', 'J', 'K', 'L',
  'M', 'N', 'O', 'P', 'Q', 'R',
  'S', 'T', 'U', 'V', 'W', 'X',
  'Y', 'Z'
]

low_range_seed = 0
high_range_seed = 25


def shift_value(low, high):
    val = random.randrange(low, high)
    return val


def encrypt(char):
    pass


my_message = "a"

shift_int = shift_value(low_range_seed, high_range_seed)
shift_int = 4

print(f'this is the shift {shift_int}')

for elem in my_message:
    if elem != ' ':
        location_as_int = alphabet.index(elem.upper())
        new_location_as_int = (location_as_int + shift_int)
        if new_location_as_int < alphabet.__len__():
            result = alphabet[new_location_as_int]
        # TODO - Handle new locations that are bigger than the length of the alphabet
    else:
        result = ''
    print(f'function result = {result}')
