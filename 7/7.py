calibration_result = 0

with open("adventofcode2024/7/7.txt", 'r') as file:
    for line in file:
        test, *operands = map(int, line.replace(':', ' ').split())
        results = [[operands[0]]]

        for i in range(1, len(operands)):
            current_results = []
            for result in results[-1]:
                current_results.append(result + operands[i])
                current_results.append(result * operands[i])
                current_results.append(int(str(result) + str(operands[i])))
            results.append(current_results)

        if test in results[-1]:
            calibration_result += test

print(calibration_result)
