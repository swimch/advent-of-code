reports = []
with open('input.txt', 'r') as f:
    for line in f:
        reports.append([int(level) for level in line.split()])

def safety(report):
    if report == sorted(report) or report == sorted(report, reverse=True):
        for i in range(1, len(report)):
            if not 1 <= abs(report[i] - report[i-1]) <= 3:
                return False
        return True
    return False

def safety2(report):
    for i in range(len(report)):
        buffer = report.pop(i)
        if safety(report):
            return True
        report.insert(i, buffer)
    return False


safe = 0
safe2 = 0
for safety_report in reports:
    if safety(safety_report):
        safe += 1
    if safety2(safety_report):
        safe2 += 1

print(f"There are {safe} safe reports with the first approach.")
print(f"There are {safe2} safe reports with the second approach.")


