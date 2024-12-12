inputs = open("adventofcode2024/9/9.txt", 'r').read()

expanded = []
id = 0

for i in range(0, len(inputs), 2):
    pair = inputs[i:i+2]
    expanded.extend([str(id)] * int(pair[0]))
    if len(pair) > 1:
        expanded.extend(['.'] * int(pair[1]))
    id += 1

result1 = expanded[:]
free_space = result1.index('.')

for i in range(len(result1) - 1, -1, -1):
    if result1[i] != ".":
        result1[free_space] = result1[i]
        result1[i] = "."
        
        free_space = result1.index('.')
        if free_space >= i:
            break

checksum1 = sum(int(item) * i for i, item in enumerate(result1) if item != '.')
print("Checksum 1:", checksum1)

result2 = expanded[:]
gaps = []
num_blocks = []
gap_start = None
start = 0

while start < len(result2):
    if result2[start] == '.':
        if gap_start is None:
            gap_start = start
    else:
        if gap_start is not None:
            gaps.append((gap_start, start - gap_start))
            gap_start = None
        block_value = result2[start]
        end = start
        while end < len(result2) and result2[end] == block_value:
            end += 1
        num_blocks.append((start, end - start, block_value))
        start = end - 1
    start += 1
if gap_start is not None:
    gaps.append((gap_start, len(result2) - gap_start))

num_blocks.reverse()

for block_start, block_size, block_value in num_blocks:
    for gap_index, (gap_start, gap_size) in enumerate(gaps):
        if gap_size >= block_size and gap_start < block_start:
            result2[gap_start:gap_start + block_size] = [block_value] * block_size
            result2[block_start:block_start + block_size] = ['.'] * block_size

            new_gap_start = gap_start + block_size
            new_gap_size = gap_size - block_size
            if new_gap_size > 0:
                gaps[gap_index] = (new_gap_start, new_gap_size)
            else:
                gaps.pop(gap_index)
            break

checksum2 = sum(int(item) * i for i, item in enumerate(result2) if item != '.')
print("Checksum 2:", checksum2)

# 6395800119709
# 6418529470362
