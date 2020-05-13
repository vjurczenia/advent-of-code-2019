def parse_int_computer(input_filename='./input.txt'):
    with open(input_filename) as input:
        str_state = input.readline().split(',')

    state = []
    for item in str_state:
        state.append(int(item))

    state[1] = 12
    state[2] = 2

    i = 0
    while i < len(state):
        if state[i] == 99:
            return state
        elif state[i] == 1:
            state[state[i+3]] = state[state[i+1]] + state[state[i+2]]
        elif state[i] == 2:
            state[state[i+3]] = state[state[i+1]] * state[state[i+2]]
        else:
            break
        i += 4

    raise Exception('Did not hit 99')

    return state
