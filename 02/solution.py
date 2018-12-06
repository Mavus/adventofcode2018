def checksum():
    contain_doubles = 0
    contain_triples = 0
    with open('input.txt', 'r') as f:
        for line in f:
            seen_counts = set()
            for char in set(line):
                char_count = line.count(char)
                seen_counts.add(char_count)
            if 2 in seen_counts:
                contain_doubles += 1
            if 3 in seen_counts:
                contain_triples += 1
        checksum_value = contain_doubles * contain_triples
        return checksum_value

def find_adjacent_ids():
    seen_lines = set()
    with open('input.txt', 'r') as f:
        for line in f:
            for previous_line in seen_lines:
                distance, common_letters = check_adjacent_ids(line, previous_line)
                if distance == 1:
                    return common_letters
            seen_lines.add(line)

def check_adjacent_ids(id1, id2):
    common_chars = [c1 for c1,c2 in zip(id1,id2) if c1 == c2]
    distance = len(id1) - len(common_chars)
    return distance, ''.join(common_chars)

print(checksum())
print(find_adjacent_ids())
