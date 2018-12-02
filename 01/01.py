from operator import add, sub

OPS = {
    '+': add,
    '-': sub
}

def part_1():
    frequency = 0
    with open('input.txt', 'r') as f:
        for line in f:
            symbol, value = line[0], int(line[1:])
            op_function = OPS[symbol]
            frequency = op_function(frequency, value) 
    return frequency

def part_2():
    frequency = 0
    previous_frequencies = set([0])
    with open('input.txt', 'r') as f:
        while True:
            for line in f:
                symbol, value = line[0], int(line[1:])
                op_function = OPS[symbol]
                frequency = op_function(frequency, value)
                if frequency in previous_frequencies:
                    return frequency
                else:
                    previous_frequencies.add(frequency)
            # At the end of the file we 'rewind' it
            f.seek(0)

print(part_1())
print(part_2())