import re
import math
import time as ti

with open('input.txt', 'r') as f:
    time = re.findall("[0-9]+", f.readline())
    distance = re.findall("[0-9]+", f.readline())
new_time = int("".join(time))
new_distance = int("".join(distance))


def check_for_win(t, d):
    start_time = ti.perf_counter()
    wins = 0
    root = math.sqrt(t ** 2 - (4 * d))
    x1 = math.floor((t + root) / 2)
    x2 = math.ceil((t - root) / 2)
    x1 = x1 - 1 if float(x1) == ((t + root) / 2) else x1
    x2 = x2 + 1 if float(x2) == ((t - root) / 2) else x2
    wins += (x1 - x2 + 1)
    runtime = ti.perf_counter() - start_time
    return wins, runtime


error_margin_1 = 1
start_time_1 = ti.perf_counter()
for i in range(len(time)):
    error_margin_1 = check_for_win(int(time[i]), int(distance[i]))[0] * error_margin_1
runtime_1 = ti.perf_counter() - start_time_1

print(f"The margin for error is {error_margin_1} in part 1. Runtime: {1e+6 * runtime_1:.2f}µs")
error_margin_2, runtime_2 = check_for_win(new_time, new_distance)
print(f"The margin for error is {error_margin_2} in part 2. Runtime: {1e+6 * runtime_2:.2f}µs")
