# loop through file, add strings with " " between them if the line isn't empty
# then extract by splitting by " " and then create dictionary by splitting again by ":"
file = []
with open('input.txt', 'r') as f:
    for line in f:
        file.append(line[:-1])
    file.append("")

passports = []
line_temp = ""
valid_passports = 0
extended_valid = 0
ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

for line in file:
    if line == "":
        passport = {}
        for field in line_temp.split():
            passport[field.split(":")[0]] = field.split(":")[1]
        passports.append(passport)
        line_temp  = ""
    else:
        if line_temp == "":
            line_temp = line
        else:
            line_temp += f" {line}"


def extended_validation(pass_check):
    if not 1920 <= int(pass_check["byr"]) <= 2002:
        return False
    if not 2010 <= int(pass_check["iyr"]) <= 2020:
        return False
    if not 2020 <= int(pass_check["eyr"]) <= 2030:
        return False
    if pass_check ["hgt"][-2:] not in ["cm", "in"]:
        return False
    elif pass_check["hgt"][-2:] == "cm":
        if not 150 <= int(pass_check["hgt"][:-2]) <= 193:
            return False
    elif pass_check["hgt"][-2:] == "in":
        if not 59 <= int(pass_check["hgt"][:-2]) <= 76:
            return False
    if (pass_check["hcl"][0] != "#" or len(pass_check["hcl"]) != 7
            or not all(c in "0123456789abcdef" for c in pass_check["hcl"][1:])):
        return False
    if pass_check["ecl"] not in ecl:
        return False
    if len(pass_check["pid"]) != 9 or not pass_check["pid"].isnumeric():
        return False
    return True


def passport_validation(pass_check, extended):
    if len(pass_check) == 8:
        if not extended:
            return True
        else:
            return extended_validation(pass_check)
    elif len(pass_check) == 7 and "cid" not in pass_check:
        if not extended:
            return True
        else:
            return extended_validation(pass_check)
    return False



### Part 1 ###
for passport in passports:
    if passport_validation(passport, False):
        valid_passports += 1
print(f"{valid_passports} passports have all required fields.")

### Part 2 ###
for passport in passports:
    if passport_validation(passport, True):
        extended_valid += 1
print(f"{extended_valid} of those are valid.")