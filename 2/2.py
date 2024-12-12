import os
import time



file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "2.txt")

safe_count = 0

def is_difference_valid(lst):  
    for i in range(len(lst) - 1):
        if abs(int(lst[i]) - int(lst[i + 1])) > 3:
            return False
    return True

def is_safe(fragments):
    return (
        (sorted(fragments) == fragments or 
         sorted(fragments, reverse=True) == fragments) and
        list(dict.fromkeys(fragments)) == fragments and
        is_difference_valid(fragments)
    )

start_time = time.time()

with open(file_path, 'r') as file:
    for line in file:
        fragments = [int(x) for x in line.split(" ")]

        if is_safe(fragments):
            safe_count += 1
        else:
            for i in range(len(fragments)):
                modified_fragments = fragments[:i] + fragments[i+1:]
                if is_safe(modified_fragments):
                    safe_count += 1
                    break

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000

print(safe_count)
print(f"Execution Time: {elapsed_time_ms:.3f} ms")


