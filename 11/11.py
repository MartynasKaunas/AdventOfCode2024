from functools import lru_cache

@lru_cache(None)
def stones(number, iters):
    if iters == 0:
        return 1

    num_str = str(number)
    length = len(num_str)

    if number == 0:
        return stones(1, iters - 1)
    
    if length % 2 == 0:
        half = length // 2
        left_half = int(num_str[:half])
        right_half = int(num_str[half:])

        left_stones = stones(left_half, iters - 1)
        right_stones = stones(right_half, iters - 1)

        return left_stones + right_stones
    else:
        multiplied = number * 2024
        return stones(multiplied, iters - 1)

# Example usage
inputs = open("adventofcode2024/11/11.txt", 'r').read().split()
iterations = 75
result = sum(stones(int(n), iterations) for n in inputs)
print(result)

# 25 197157
# 75 234430066982597