import re
import numpy as np

numbers = list(map(int, re.findall(r'\d+', open('adventofcode2024/13/13.txt', 'r').read())))

machines_list = []
for i in range(0, len(numbers), 6):
    chunk = numbers[i:i+6]
    machines_list.append([
        [chunk[0], chunk[2], chunk[4]],
        [chunk[1], chunk[3], chunk[5]]
    ])

machines = np.array(machines_list)

for offset in (0, 1e13):
    results = 0
    for i, machine in enumerate(machines):
        steps = machine[:, :2]
        prize = machine[:, 2:] + offset

        # https://numpy.org/doc/2.1/reference/generated/numpy.linalg.solve.html
        result = np.linalg.solve(steps, prize).round().astype(int)

        x, y = result.squeeze()
        
        if np.allclose(np.dot(steps, result), prize, atol=1e-14, rtol=1e-14):
            results += (x * 3 + y)

        # print(f"Machine {i + 1}:")
        # for j, (step, prize_value) in enumerate(zip(steps, prize)):
        #     print(f"  {step[0]}*X + {step[1]}*Y = {prize_value[0]}")
        # print(f"  Solution: X = {x}, Y = {y}\n")

    print("Result:", results)

# 38714
# 74015623345775