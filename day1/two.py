from math import floor

def get_more_fuel_requirements_sum(input_filepath='./input.txt'):
    total = 0
    with open(input_filepath) as input:
        for line in input:
            cur_fuel = floor(int(line) / 3) - 2
            pre_total = 0
            while cur_fuel > 0:
                pre_total += cur_fuel
                cur_fuel = floor(int(cur_fuel) / 3) - 2
            total += pre_total
    return total