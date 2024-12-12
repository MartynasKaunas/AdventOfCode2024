import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "1.txt")

distance_sum = 0
similarity_score = 0

def build_lists():
    list1 = []
    list2 = []

    with open(file_path, 'r') as file:
        for index, line in enumerate(file, start=1):
            line = line.strip()
            fragments = line.split("   ")

            list1.append(fragments[0])
            list2.append(fragments[1])

    list1.sort()
    list2.sort()

    return list1, list2

a, b = build_lists()

for itemA, itemB in zip(a, b):
    occ = b.count(itemA)
    similarity_score += int(itemA) * occ

    itemA = int(itemA)
    itemB = int(itemB)
    if itemA > itemB:
        distance_sum += itemA-itemB
    elif itemA < itemB:
        distance_sum += itemB-itemA

print(distance_sum)
print(similarity_score)