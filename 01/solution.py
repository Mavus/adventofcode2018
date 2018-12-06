from operator import add, sub

OPS = {
    '+': add,
    '-': sub
}

def total_frequency():
    frequency = 0
    with open('input.txt', 'r') as f:
        for line in f:
            symbol, value = line[0], int(line[1:])
            op_function = OPS[symbol]
            frequency = op_function(frequency, value) 
    return frequency

def first_reoccuring_freq():
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

print(total_frequency())
print(first_reoccuring_freq())