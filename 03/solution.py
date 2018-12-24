import re


def count_overlaps():
    fabric = [[None for _ in range(10000)] for _ in range(10000)]
    overlap_map = set()

    with open('input.txt', 'r') as f:
        for line in f:
            claim_data = re.findall(r'\d+', line)
            claim_id, x_coord, y_coord, width, height = map(int, claim_data)
            
            for x in range(x_coord, x_coord + width):
                for y in range(y_coord, y_coord + height):
                    if fabric[x][y]:
                        overlap_map.add("{},{}".format(x,y))
                    else:
                        fabric[x][y] = True
    return len(overlap_map)

def find_uncontested_square():
    fabric = [[None for _ in range(10000)] for _ in range(10000)]
    uncontested_squares = set()
    with open('input.txt', 'r') as f:
        for line in f:
            claim_data = re.findall(r'\d+', line)
            claim_id, x_coord, y_coord, width, height = map(int, claim_data)
            this_claim_uncontested = True
            for x in range(x_coord, x_coord + width):
                for y in range(y_coord, y_coord + height):
                    previous_claim = fabric[x][y]
                    if previous_claim:
                        try:
                            uncontested_squares.remove(previous_claim)
                        except KeyError:
                            pass
                        this_claim_uncontested = False
                    else:
                        fabric[x][y] = claim_id
            if this_claim_uncontested:
                uncontested_squares.add(claim_id)
    return uncontested_squares

print(count_overlaps())
print(find_uncontested_square())