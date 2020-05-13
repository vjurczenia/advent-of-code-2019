from math import floor

def get_fuel_requirements_sum(input_filepath='./input.txt'):
    total = 0
    with open(input_filepath) as input:
        for line in input:
            total += floor(int(line) / 3) - 2
    return total